from django.db import models


class Coord(models.Model):
    """Модель список координат города."""
    town = models.ForeignKey('Town', models.CASCADE)
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'coord'


class Telegram(models.Model):
    """Модель пользователя телеграм."""
    id = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    fname = models.CharField(max_length=45, blank=True, null=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    create_dt = models.DateTimeField(blank=True, null=True)
    update_dt = models.DateTimeField(blank=True, null=True)
    delete_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'telegram'


class Town(models.Model):
    """Модель список городов."""
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = True
        db_table = 'town'


class WeatherOwm(models.Model):
    """Модель метеоданные по городу с сайта https://openweathermap.org."""
    town = models.ForeignKey(Town, models.CASCADE)
    time_ts = models.DateTimeField()
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    site = models.CharField(max_length=15)
    create_dt = models.DateTimeField(blank=True, null=True)
    update_dt = models.DateTimeField(blank=True, null=True)
    delete_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'weather_owm'


class WeatherWb(models.Model):
    """Модель метеоданные по городу с сайта https://weatherbit.io."""
    town = models.ForeignKey(Town, models.CASCADE)
    time_ts = models.DateTimeField()
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    site = models.CharField(max_length=15)
    create_dt = models.DateTimeField(blank=True, null=True)
    update_dt = models.DateTimeField(blank=True, null=True)
    delete_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'weather_wb'


# from django.contrib.auth.models import User
# user = User.objects.create_user(username="", email="", password="")


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
