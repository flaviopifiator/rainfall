from rest_framework.routers import DefaultRouter

from rainfall.floor.urls import url_api_floor


app_name = "api"

urlpatterns = []
urlpatterns += url_api_floor
