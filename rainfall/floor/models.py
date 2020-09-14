from decimal import Decimal

from django.db import models

from djgeojson.fields import PointField

from .managers import RainManager, FloorManager


class Floor(models.Model):
    name = models.CharField(max_length=250)
    hectares = models.DecimalField(max_digits=12, decimal_places=2)
    point = PointField()
    objects = FloorManager()

    def __str__(self) -> str:
        return f'{self.name}'

    def avarage_precipitations(self, days) -> Decimal:
        return self.rains.filter_last_days(days).aggregate(models.Avg('precipitation')) \
            .get('precipitation__avg')

    @property
    def longitude(self):
        try:
            longitude = self.point.get('coordinates')[0]
        except IndexError:
            longitude = None
        return longitude

    @property
    def latitude(self):
        try:
            latitude = self.point.get('coordinates')[1]
        except IndexError:
            latitude = None
        return latitude
        

class Rain(models.Model):
    date = models.DateTimeField()
    precipitation = models.DecimalField(max_digits=6, decimal_places=3)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rains')
    objects = RainManager()

    def __str__(self) -> str:
        return f'{self.floor.name}, {self.date}'
    