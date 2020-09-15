from decimal import Decimal

from django.test import TestCase
from django.utils import timezone

from rest_framework.test import APIClient
from rest_framework import status

from .factories import FloorFactory, RainFactory
from .models import Floor, Rain
from .api.serializers import FloorSerializer, RainSerializer


api_client = APIClient()


class FloorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.floor_1 = FloorFactory(
            id=1, name='floor_1', hectares=Decimal(123.34)
        )
        cls.floor_2 = FloorFactory(
            id=2, name='floor_2', hectares=Decimal(111.33)
        )
        cls.rain_1 = RainFactory(
            floor=cls.floor_1, date=timezone.now()-timezone.timedelta(days=1),
            precipitation=Decimal('100.50')
        )
        cls.rain_2 = RainFactory(
            floor=cls.floor_1, date=timezone.now()-timezone.timedelta(days=5),
            precipitation=Decimal('200.76')
        )
        cls.rain_3 = RainFactory(
            floor=cls.floor_1, date=timezone.now()-timezone.timedelta(days=6),
            precipitation=Decimal('590.00')
        )
        cls.rain_4 = RainFactory(
            floor=cls.floor_1, date=timezone.now()-timezone.timedelta(days=8),
            precipitation=Decimal('730.14')
        )
        cls.rain_5 = RainFactory(
            floor=cls.floor_2, date=timezone.now()-timezone.timedelta(days=10),
            precipitation=Decimal('350.10')
        )
        cls.rain_6 = RainFactory(
            floor=cls.floor_2, date=timezone.now()-timezone.timedelta(days=10),
            precipitation=Decimal('500.15')
        )

    def test_average_precipitations(self):
        avg_expected_1 = Decimal('100.50')
        self.assertEqual(self.floor_1.average_precipitations(2), avg_expected_1)
        
        avg_expected_2 = Decimal('297.09')
        self.assertEqual(self.floor_1.average_precipitations(7), avg_expected_2)

        avg_expected_3 = Decimal(0)
        self.assertEqual(self.floor_1.average_precipitations(1), avg_expected_3)

    def test_viewset_all_floor(self):
        response = api_client.get('/api/v1/floor/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        floor_serializer = FloorSerializer(Floor.objects.all(), many=True)
        self.assertEqual(response.json(), floor_serializer.data)

    def test_viewset_floor_last_day(self):
        url = '/api/v1/floor/?last_days={}'
        
        response = api_client.get(url.format(2))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        data_expected = [
            {'id': 1, 'name': 'floor_1', 'hectares': '123.34', 'precipitations': '100.50'},
            {'id': 2, 'name': 'floor_2', 'hectares': '111.33'}
        ]
        self.assertEqual(data, data_expected)

        response = api_client.get(url.format(7))
        data = response.json()
        data_expected = [
            {'id': 1, 'name': 'floor_1', 'hectares': '123.34', 'precipitations': '297.09'},
            {'id': 2, 'name': 'floor_2', 'hectares': '111.33'}
        ]
        self.assertEqual(data, data_expected)

    def test_viewset_floor_precipitations_greater(self):
        url = '/api/v1/floor/?precipitations__gt={}'
        
        response = api_client.get(url.format('20000'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        data_expected = []
        self.assertEqual(data, data_expected)
        
        response = api_client.get(url.format('900'))
        data = response.json()
        data_expected = [{'id': 1, 'name': 'floor_1', 'hectares': '123.34'}]
        self.assertEqual(data, data_expected)

    def test_viewset_rain(self):
        response = api_client.get('/api/v1/rain/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        rain_serializer = RainSerializer(Rain.objects.all(), many=True)
        self.assertEqual(response.json(), rain_serializer.data)

    def test_viewset_rain_filter_floor(self):
        response = api_client.get('/api/v1/rain/?floor__name=floor_1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 4)

        response = api_client.get('/api/v1/rain/?floor__id=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
