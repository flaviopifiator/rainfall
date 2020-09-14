from django.conf import settings

from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError

from rainfall.floor.models import Floor
from rainfall.floor.models import Rain

from .serializers import FloorSerializer
from .serializers import RainSerializer
from .filters import FloorFilter


class FloorViewSet(ListModelMixin, GenericViewSet):
    """This view returns the list of floors
    
    query_params:
    last_days=int Returns the average rainfall, last_days takes values between 1 and 7.
    precipitations__gt=decimal Filters those soils where their historical precipitation is higher than the declared value.

    allow_methods:
    GET
    """
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    filterset_class = FloorFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        last_days = self.get_last_days_params()
        if last_days:
            context['last_days'] = last_days
        return context

    def get_last_days_params(self):
        last_days = None
        param_last_days = self.request.query_params.get('last_days')
        if param_last_days:
            if isinstance(param_last_days, str) and param_last_days.isdigit():
                param_last_days = int(param_last_days)
                if settings.MIN_DAYS_RAIN <= param_last_days <= settings.MAX_DAYS_RAIN:
                    last_days = param_last_days
                else:
                    raise ValidationError({'params': ['last_days filter between 1 and 7 days']})     
            else:
                raise ValidationError({'params': ['last_days must be an integer']})
        return last_days


class RainViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    """This viewset returns the list of rains, and allows to create a new record.
    
    query_params:
    precipitations__gt=decimal Filters those soils where their historical precipitation is higher than the declared value.

    allow_methods:
    GET, POST
    """
    queryset = Rain.objects.all()
    serializer_class = RainSerializer
    filterset_fields = ('floor__name', 'floor__id')
    