import json
import datetime

from django.http import HttpResponse, JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.forms.models import model_to_dict

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from .models import Town, Coord, WeatherOwm, WeatherWb, Telegram
from .forms import TOWNS_ADD_SCHEMA, TOWNS_GET_SCHEMA
from weather_app.owm import OWMRequest
from weather_app.wb import WBRequest


# FIXME:
#  CHECK this way:
#  1)
#  curl -v -H "Content-Type: application/json" -X POST -d
#  '{"town_list": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Chelyabinsk",
#  "Volgograd", "Magnitogorsk", "Kemerovo", "Vladimir"]}'
#  http://127.0.0.1:8000/api/v1/weather/town/
#  2)
#  curl -v -H "Content-Type: application/json" -X POST
#  http://127.0.0.1:8000/api/v1/weather/town/1/
#  3)
#  curl -v -H "Content-Type: application/json" -X POST
#  http://127.0.0.1:8000/api/v1/weather/town/1/5/
#  4)
#  curl -v -H "Content-Type: application/json" -X GET
#  http://127.0.0.1:8000/api/v1/weather/town/get_all/


@method_decorator(csrf_exempt, name='dispatch')
class AddTownView(View):
    """View для добавления списка городов."""

    def post(self, request):
        try:
            data = json.loads(request.body)
            validate(data, TOWNS_ADD_SCHEMA)

            data_dict = dict()
            for twn in data['town_list']:
                if not Town.objects.filter(name=twn).exists():
                    item = Town(name=twn)
                    item.save()
                    data_dict[twn] = item.pk
                else:
                    ex_item = Town.objects.get(name=twn)
                    data_dict[twn] = ex_item.pk
                    # print(f"Town {twn} already exists! id: {ex_item.pk}")

            site_owm = write_to_db_owm(data_dict=data_dict)
            site_wb = write_to_db_wb(data_dict=data_dict)

            # town_db2 = Town.objects.order_by('id').values()
            # town_db = Town.objects.all()

            return JsonResponse(data=data_dict, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
        # except TypeError as err:
        #     return JsonResponse({'errors': 'ResponseError'}, status=400)
        # except OWMError as err:
        #     return JsonResponse({'errors': 'OpenWeatherMapServerError'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class GetTownWeatherView(View):
    """View для запроса погоды по одному городу."""

    def post(self, request, item_id):
        try:
            # data = json.loads(request.body)
            # validate(data, TOWNS_ADD_SCHEMA)

            item_town = Town.objects.get(id=item_id)
            items1 = WeatherOwm.objects.filter(town_id=item_id)
            items2 = WeatherWb.objects.filter(town_id=item_id)

            items_twn = model_to_dict(item_town)
            items_1 = {model_to_dict(x)['id']: (model_to_dict(x)) for x in items1}
            items_2 = {model_to_dict(x)['id']: (model_to_dict(x)) for x in items2}

            for it1 in items_1.values():
                it1['time_ts'] = datetime.datetime.strftime(it1['time_ts'], "%Y:%m:%d %H:%M:%S.%f")
                it1['temperature'] = str(it1['temperature'])
                it1['town'] = items_twn['name']
                it1['id'] = items_twn['id']
            for it2 in items_2.values():
                it2['time_ts'] = datetime.datetime.strftime(it2['time_ts'], "%Y:%m:%d %H:%M:%S.%f")
                it2['temperature'] = str(it2['temperature'])
                it2['town'] = items_twn['name']
                it2['id'] = items_twn['id']

            send_data = {items_twn['name']: [json.dumps(items_1), json.dumps(items_2)]}

            return JsonResponse(send_data, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
        except Town.DoesNotExist:
            return JsonResponse({'errors': 'town does not exist! insert it first: api/v1/weather/town/'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class GetTownsWeatherView(View):
    """View для запроса погоды по нескольким городам."""

    def post(self, request, item_start, item_stop):
        try:
            # data = json.loads(request.body)
            # validate(data, TOWNS_ADD_SCHEMA)
            if item_start >= item_stop:
                raise ItemStartStopError
            if item_stop - item_stop > 10:
                item_stop = item_start + 9

            items_town = Town.objects.filter(id__gte=item_start, id__lte=item_stop)
            items1 = WeatherOwm.objects.filter(town_id__gte=item_start, town_id__lte=item_stop)
            items2 = WeatherWb.objects.filter(town_id__gte=item_start, town_id__lte=item_stop)

            items_twn = [model_to_dict(x) for x in items_town]
            items_1 = {model_to_dict(x)['id']: model_to_dict(x)
                       for x in items1
                       for twn in items_town
                       if model_to_dict(twn)['id'] == model_to_dict(x)['town']}
            items_2 = {model_to_dict(x)['id']: model_to_dict(x)
                       for x in items2
                       for twn in items_town
                       if model_to_dict(twn)['id'] == model_to_dict(x)['town']}

            for it1 in items_1.values():
                it1['time_ts'] = datetime.datetime.strftime(it1['time_ts'], "%Y:%m:%d %H:%M:%S.%f")
                it1['temperature'] = str(it1['temperature'])
                for tw in items_twn:
                    if tw['id'] == it1['town']:
                        it1['town'] = tw['name']
                        it1['id'] = tw['id']
            for it2 in items_2.values():
                it2['time_ts'] = datetime.datetime.strftime(it2['time_ts'], "%Y:%m:%d %H:%M:%S.%f")
                it2['temperature'] = str(it2['temperature'])
                for tw in items_twn:
                    if tw['id'] == it2['town']:
                        it2['town'] = tw['name']
                        it2['id'] = tw['id']

            send_data = {f'{item_start}-{item_stop}': [json.dumps(items_1), json.dumps(items_2)]}

            return JsonResponse(send_data, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
        except Town.DoesNotExist:
            return JsonResponse({'errors': 'DoesNotExistError! '
                                           'town does not exist! insert it first: api/v1/weather/town/'}, status=404)
        except ItemStartStopError as err:
            return JsonResponse({'errors': 'ItemStartStopError! '
                                           'try to make correct response: api/v1/weather/town/1/3/'}, status=400)


def write_to_db_owm(data_dict):
    for twn, twn_id in data_dict.items():
        owm_resp = OWMRequest(twn).make_request()
        coord = owm_resp.json()['coord']
        temp_dict = owm_resp.json()['main']
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='milliseconds')

        if not Coord.objects.filter(town_id=twn_id).exists():
            item_coord = Coord(town_id=twn_id,
                               latitude=coord['lat'],
                               longitude=coord['lon'],
                               )
            item_coord.save()

        item_wth = WeatherOwm(town_id=twn_id,
                              time_ts=timestamp,
                              temperature=temp_dict['temp'],
                              site='OpenWeatherMap'
                              )
        item_wth.save()

    return {'site': 'OpenWeatherMap'}


def write_to_db_wb(data_dict):
    for twn, twn_id in data_dict.items():
        wb_resp = WBRequest(twn).make_request()
        coord_lat = wb_resp.json()['data'][0]['lat']
        coord_lon = wb_resp.json()['data'][0]['lon']
        temp = wb_resp.json()['data'][0]['temp']
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='milliseconds')

        if not Coord.objects.filter(town_id=twn_id).exists():
            item_coord = Coord(town_id=twn_id,
                               latitude=coord_lat,
                               longitude=coord_lon,
                               )
            item_coord.save()

        item_wth = WeatherWb(town_id=twn_id,
                             time_ts=timestamp,
                             temperature=temp,
                             site='WeatherBit'
                             )
        item_wth.save()
    return {'site': 'WeatherBit'}


class OWMError(Exception):
    """exception class OWMError"""
    pass


class WBError(Exception):
    """exception class WBError"""
    pass


class ItemStartStopError(Exception):
    """exception class ItemStartStopError"""
    pass