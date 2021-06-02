# -*- encoding: utf-8 -*-
import os
import json

from decouple import config
import requests
from requests import Response


WB_API_KEY = config('WB_API_KEY')
WB_API_URL = config('WB_API_URL', default='http://api.weatherbit.io/v2.0/current')

# link = 'https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Current32Weather32Data/get_current_city_id_city_id'


class WBRequest:
    """
    Insert Town for API request to https://weatherbit.io

    Then use method:
        make_request()
    """
    def __init__(self, town: str):
        self.town = town
        self.params = {
            'city': self.town,
            'key': WB_API_KEY,
            'units': 'M'
        }

    def make_request(self):
        response = requests.get(WB_API_URL, params=self.params)
        try:
            if response:
                coord1 = response.json()['data'][0]['lat']
                coord2 = response.json()['data'][0]['lon']
                temp_dict = response.json()['data'][0]['temp']
        except Exception as e:
            return
        return response


# xx = WBRequest('M').make_request()
#
# print(WB_API_KEY)
# print(xx.status_code)
# print(xx.headers.get('Content-Type'))
# print(xx.json())
