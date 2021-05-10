import json
import os

import pytest
from decouple import config

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
    assert config('ENV_MYSQL_DATABASE') is not None
    assert config('ENV_MYSQL_USER') is not None
    assert config('ENV_MYSQL_PASSWORD') is not None
    assert config('ENV_MYSQL_ROOT_PASSWORD') is not None
    assert config('ENV_MYSQL_TIMEZONE') is not None


def test_owm():
    owm = OWMRequest('Moscow')
    assert owm.make_request().status_code == 200


def test_wb():
    wb = WBRequest('Moscow')
    assert wb.make_request().status_code == 200
    print('ok')

