from typing import List

import requests
from requests import Response
from decouple import config


DJANGO_HOST = config('ENV_DJANGO_HOST', default='0.0.0.0')
DJANGO_PORT = config('ENV_DJANGO_PORT', default='8000')
PROTOCOL = config('ENV_API_PROTOCOL', default='http')


class ApiRequests:

    api_req = '/api/v1/weather/town/'
    url = f'{PROTOCOL}://{DJANGO_HOST}:{DJANGO_PORT}{api_req}'

    @classmethod
    def send_town_list(cls, *args: List[str]) -> Response:
        if args:
            data = {
                "town_list": list(args)
            }
        else:
            data = {
                "town_list": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Chelyabinsk",
                              "Volgograd", "Magnitogorsk", "Kemerovo", "Vladimir"]
            }
        response = requests.post(cls.url, json=data)  #, content_type='application/json')
        return response

    @classmethod
    def get_one_town(cls, arg: int) -> Response:
        if arg:
            url = f'{cls.url}{arg}/'
        else:
            url = f'{cls.url}1/'
        response = requests.post(url)
        return response

    @classmethod
    def get_many_towns(cls, arg1: int, arg2: int) -> Response:
        if arg1 and arg2:
            url = f'{cls.url}{arg1}/{arg2}/'
        else:
            url = f'{cls.url}1/5/'
        response = requests.post(url)
        return response
