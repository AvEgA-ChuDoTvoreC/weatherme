import json
import datetime

from django import forms
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


# FIXME: There is some kinda problem which don't wanna read json response while using Django forms; BUT jsonschema - OK
#  CHECK this way:
#  1)
#  curl -v -H "Content-Type: application/json" -X POST -d
#  '{"town_list": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Chelyabinsk",
#  "Volgograd", "Magnitogorsk", "Kemerovo", "Vladimir"]}'
#  http://127.0.0.1:8000/api/v1/weather/town/
#  2)
#  curl -v -H "Content-Type: application/json" -X POST -d
#  '{"text": "Best. Cheese. Ever.", "grade": 9}'
#  http://127.0.0.1:8000/api/v1/weather/town/1/
#  3)
#  curl -v -H "Content-Type: application/json" -X GET
#  http://127.0.0.1:8000/api/v1/weather/town/get_all/


@method_decorator(csrf_exempt, name='dispatch')
class AddTownView(View):
    """View для добавления списка городов."""

    def post(self, request):
        try:
            data = json.loads(request.body)
            print(data)
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
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        try:
            # item = Item.objects.get(id=item_id)
            data = json.loads(request.body)
            # validate(data, GOODS_REVIEW_SCHEMA)
            # review = Review(grade=data['grade'],
            #                 text=data['text'],
            #                 item=item)
            # review.save()

            # return JsonResponse({"id": review.id}, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
        # except Item.DoesNotExist:
        #     return JsonResponse({}, status=404)


class GetTownsWeatherView(View):
    """View для получения метеоданных по всем городам.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        pass
        try:
            print("info: ", item_id)
            item = Item.objects.prefetch_related('review_set').get(id=item_id)
            print("item_info: ", item)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
        data = model_to_dict(item)
        item_views = [model_to_dict(x) for x in item.review_set.all()]
        item_views = sorted(item_views, key=lambda review: review['id'], reverse=True)[:5]
        print("item_info: ", data, item_views)
        for review in item_views:
            review.pop('item', None)
        data['reviews'] = item_views
        return JsonResponse(data, status=200)


class OWMError(Exception):
    """exception class OWMError"""
    def __init__(self, err=None):
        self.error = err

    def message(self):
        return f"OpenWeatherMap ERROR"


class WBError(Exception):
    """exception class WBError"""
    pass


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
