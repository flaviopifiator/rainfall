from django.db.models import Sum

from django_filters import rest_framework as filters

from rainfall.floor.models import Floor


class FloorFilter(filters.FilterSet):
    precipitations__gt = filters.NumberFilter(method='get_greater_precipitations')

    def get_greater_precipitations(self, queryset, field_name, value):
        return Floor.objects.sum_precipitations_greater(value, queryset=queryset)
