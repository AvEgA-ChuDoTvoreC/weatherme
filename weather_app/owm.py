# -*- encoding: utf-8 -*-
import os
import json

from decouple import config
import requests
from requests import Response


OWM_API_KEY = config('OWM_API_KEY')  # , default='11c0d3dc6093f7442898ee49d2430d20')
OWM_API_URL = config('OWM_API_URL', default='https://api.openweathermap.org/data/2.5/weather')

# link = 'https://openweathermap.org/current#current_JSON'
# alll = 'http://api.openweathermap.org/data/2.5/group?id=
# 524901,703448,2643743&units=metric&appid=11c0d3dc6093f7442898ee49d2430d20'


class OWMRequest:
    """
    Insert Town for API request to https://openweathermap.org/

    Then use method:
        make_request()
    """
    def __init__(self, town: str):
        self.town = town
        self.params = {
            'q': self.town,
            'appid': OWM_API_KEY,
            'units': 'metric'
        }

    def make_request(self):
        response = requests.get(OWM_API_URL, params=self.params)
        try:
            coord = response.json()['coord']
            temp_dict = response.json()['main']
            # print(coord)
            # print(temp_dict)
        except Exception as e:
            return
        return response


# xx = OWMRequest('Moscow').make_request()
#
# print(OWM_API_KEY)
# print(xx.status_code)
# print(xx.headers['Content-Type'])
# print(xx.json())
# data = xx.json()
# template = 'Current temperature in {} is {}'
# print(template.format('Moscow', data['main']['temp']))
