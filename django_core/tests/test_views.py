import json
import os

import pytest
from decouple import config

from api.models import Coord, WeatherWb, WeatherOwm, Town, Telegram
from weather_app.owm import OWMRequest
from weather_app.wb import WBRequest


def test_env():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file = '.env'
    find_env = os.path.join(base_dir, file)
    assert os.path.exists(find_env) is True


def test_env_param():
    x = config('DEBUG')
    assert config('OWM_API_URL') == 'https://api.openweathermap.org/data/2.5/weather'
    assert config('WB_API_URL') == 'http://api.weatherbit.io/v2.0/current'
    assert x == 'True'
    assert config('OWM_API_KEY') is not None
    assert config('WB_API_KEY') is not None
    assert config('SECRET_KEY') is not None


def test_owm():
    owm = OWMRequest('Moscow')
    assert owm.make_request().status_code == 200


def test_wb():
    wb = WBRequest('Moscow')
    assert wb.make_request().status_code == 200
    print('ok')


class TestViews(object):

    def test_post_town(self, client, db):
        """
        /api/v1/weather/town/ (POST) сохраняет города в базе.
        :return словарь {город: id}
        """
        url = '/api/v1/weather/town/'
        data = json.dumps({
            "town_list": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Chelyabinsk",
                          "Volgograd", "Magnitogorsk", "Kemerovo", "Vladimir"]
        })
        response = client.post(url, data=data, content_type='application/json')
        assert response.status_code == 201
        document = response.json()
        # Объект был сохранен в базу
        for twn in document:
            item = Town.objects.get(pk=document[twn])
            assert item.name == twn

    def test_post_town_1(self, client, db):
        """
        /api/v1/weather/town/1/ (POST) получить город по :id."""
        url = '/api/v1/weather/town/1/'
        data = json.dumps({})
        response = client.post(url, data=data, content_type='application/json')
        assert response.status_code == 404




