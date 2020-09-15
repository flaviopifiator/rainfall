from rest_framework import serializers

from rainfall.floor.models import Floor
from rainfall.floor.models import Rain


class FloorSerializer(serializers.ModelSerializer):
    precipitations = serializers.SerializerMethodField('avg_precipitations')

    def avg_precipitations(self, obj):
        last_days = self.context.get('last_days')
        if last_days:
            return obj.average_precipitations(last_days)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['precipitations']:
            data.pop('precipitations')
        else:
            data['precipitations'] = str(data['precipitations'])
        return data

    class Meta:
        model = Floor
        fields = [
            'id', 'name', 'hectares', 'latitude', 'longitude', 'precipitations'
        ]


class RainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rain
        fields = '__all__'
