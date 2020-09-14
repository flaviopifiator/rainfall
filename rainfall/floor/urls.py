from rest_framework.routers import DefaultRouter

from .api.viewsets import FloorViewSet
from .api.viewsets import RainViewSet


app_name = 'floor'

router = DefaultRouter()
router.register(r'floor', FloorViewSet)
router.register(r'rain', RainViewSet)

url_api_floor = []
url_api_floor += router.urls