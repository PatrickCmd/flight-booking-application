from django.urls import path
from .views import (FlightListCreateView,
                    FlightRetrieveUpdateDeleteView,)


app_name = 'flight'

urlpatterns = [
    path('flights/', FlightListCreateView.as_view(), name='list_create_flight'),
    path('flights/<pk>', FlightRetrieveUpdateDeleteView.as_view(),
         name='flight_details'),
]
