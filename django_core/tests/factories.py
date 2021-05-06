import factory
import factory.fuzzy


# class aaFactory(factory.django.DjangoModelFactory):
#
#     title = factory.Sequence(lambda n: '{}'.format(n))
#     description = factory.Sequence(
#         lambda n: 'Desc{}'.format(n)
#     )
#     price = factory.fuzzy.FuzzyInteger(1, 100000)
#
#
#
# class ddFactory(factory.django.DjangoModelFactory):
#
#     grade = factory.fuzzy.FuzzyInteger(1, 10)
#     text = factory.Sequence(lambda n: 'Test {}'.format(n))
#     item = factory.SubFactory(ItemFactory)



class TownFactory(factory.django.DjangoModelFactory):
    """Модель список городов."""
    name = factory.Sequence('Moscow')

    class Meta:
        model = 'django_core.api.Town'


class CoordFactory(factory.django.DjangoModelFactory):
    """Модель список координат города."""
    town = factory.SubFactory(TownFactory)
    latitude = factory.fuzzy.FuzzyDecimal(00.0001, 99.9999)
    longitude = factory.fuzzy.FuzzyDecimal(00.0001, 99.9999)

    class Meta:
        model = 'django_core.api.Coord'


# class WeatherOwmFactory(factory.django.DjangoModelFactory):
#     """Модель метеоданные по городу с сайта https://openweathermap.org."""
#     town = models.ForeignKey(Town, models.CASCADE)
#     time_ts = models.DateTimeField()
#     temperature = models.DecimalField(max_digits=4, decimal_places=2)
#     site = models.CharField(max_length=15)
#     create_dt = models.DateTimeField(blank=True, null=True)
#     update_dt = models.DateTimeField(blank=True, null=True)
#     delete_dt = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         model = 'django_core.api.WeatherOwm'
#
#
# class WeatherWbFactory(factory.django.DjangoModelFactory):
#     """Модель метеоданные по городу с сайта https://weatherbit.io."""
#     town = models.ForeignKey(Town, models.CASCADE)
#     time_ts = models.DateTimeField()
#     temperature = models.DecimalField(max_digits=4, decimal_places=2)
#     site = models.CharField(max_length=15)
#     create_dt = models.DateTimeField(blank=True, null=True)
#     update_dt = models.DateTimeField(blank=True, null=True)
#     delete_dt = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         model = 'django_core.api.WeatherWb'

