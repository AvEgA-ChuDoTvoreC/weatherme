from django.urls import path
from django.conf.urls import url

from .views import AddTownView, GetTownWeatherView, GetTownsWeatherView


urlpatterns = [
    path('api/v1/weather/town/', AddTownView.as_view()),
    path('api/v1/weather/town/<int:item_id>/', GetTownWeatherView.as_view()),
    path('api/v1/weather/town/get_all/', GetTownsWeatherView.as_view()),
]
