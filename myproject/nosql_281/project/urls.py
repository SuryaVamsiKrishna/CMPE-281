from django.urls import path
from . import views
from .views import AVVehicleList, SensorList, TripList, DataList

urlpatterns = [
    path('api/av_vehicles/', AVVehicleList.as_view(), name='av_vehicles'),
    path('api/sensors/', SensorList.as_view(), name='sensors'),
    path('api/trips/', TripList.as_view(), name='trips'),
    path('api/data/', DataList.as_view(), name='data'),

]