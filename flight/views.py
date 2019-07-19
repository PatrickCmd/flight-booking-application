import math

from django.shortcuts import render

from rest_framework.exceptions import (PermissionDenied,
                                       ValidationError)
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .serializers import FlightSerializer
from .renderers import FlightRenderer
from .models import Flight, Seat
from .utils import generate_seats


class FlightListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (FlightRenderer,)
    serializer_class = FlightSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied("You don't have permissions to carry out this action.")
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        flight = serializer.save(created_by=self.request.user)
        seats_per_row = 9
        row_count = math.ceil(serializer.data['capacity'] / seats_per_row)
        generate_seats(Seat, flight, start_row=1, row_count=row_count,
                       seats_per_row=seats_per_row)


class FlightRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (FlightRenderer,)
    serializer_class = FlightSerializer

    queryset = Flight.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied("You don't have permissions to carry out this action.")
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied("You don't have permissions to carry out this action.")
        return super().destroy(request, *args, **kwargs)
