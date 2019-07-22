from django.urls import path
from .views import (FlightListCreateView,
                    FlightRetrieveUpdateDeleteView,
                    ReservationListCreateView,
                    ReservationRetrieveDestroyAPIView,
                    CancelReservationAPIView,
                    flight_reservation_count,)


app_name = 'flight'

urlpatterns = [
    path('flights/', FlightListCreateView.as_view(), name='list_create_flight'),
    path('flights/<pk>', FlightRetrieveUpdateDeleteView.as_view(),
         name='flight_details'),
    path('flights/<pk>/reservations', ReservationListCreateView.as_view(),
         name='list_make_reservations'),
    path('flights/<flight_pk>/reservations/<pk>', ReservationRetrieveDestroyAPIView.as_view(),
         name='reservation_details'),
    path('flights/<flight_pk>/reservations/<pk>/cancel', CancelReservationAPIView.as_view(),
         name='cancel_reservation'),
    path('reservations/<flight_pk>/count/<date>/',
         flight_reservation_count,
         name='count_flight_reservations'),
]
