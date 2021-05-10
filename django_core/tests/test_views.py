import json

import pytest

from api.models import Coord, WeatherWb, WeatherOwm, Town, Telegram


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




