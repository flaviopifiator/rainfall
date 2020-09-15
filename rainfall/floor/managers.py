from django.db import models
from django.utils import timezone


class FloorManager(models.Manager):

    def sum_precipitations_greater(self, precipitation, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return queryset.annotate(sum_precipitation=models.Sum('rains__precipitation')) \
            .filter(sum_precipitation__gt=precipitation)


class RainManager(models.Manager):

    def filter_last_days(self, days:int):
        date = timezone.now() - timezone.timedelta(days=days)
        return self.get_queryset().filter(date__gte=date)
