import math

from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .serializers import FlightSerializer, ReservationSerializer
from .renderers import FlightRenderer, ReservationRenderer
from .models import Flight, Seat, Reservation
from .utils import generate_seats


class FlightListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (FlightRenderer,)
    serializer_class = FlightSerializer

    queryset = Flight.objects.all()

    def create(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied(
                "You don't have permissions to carry out this action."
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        flight = serializer.save(created_by=self.request.user)
        seats_per_row = 9
        row_count = math.ceil(serializer.data["capacity"] / seats_per_row)
        generate_seats(
            Seat, flight, start_row=1, row_count=row_count, seats_per_row=seats_per_row
        )


class FlightRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (FlightRenderer,)
    serializer_class = FlightSerializer

    queryset = Flight.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied(
                "You don't have permissions to carry out this action."
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied(
                "You don't have permissions to carry out this action."
            )
        return super().destroy(request, *args, **kwargs)


class ReservationListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ReservationRenderer,)
    serializer_class = ReservationSerializer

    def get_queryset(self):
        qs = Reservation.objects.all()
        if self.request.user.is_admin:
            queryset = qs
        else:
            queryset = qs.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        flight = Flight.objects.get(pk=self.kwargs.get("pk"))
        try:
            seat = Seat.objects.get(
                seat_number=self.request.data["seat"], flight=flight
            )
            if not seat.is_available:
                raise ValidationError("Seat is not available")
        except Seat.DoesNotExist:
            raise ValidationError("Not a valid seat")
        seat.is_available = False
        seat.save()
        serializer.save(user=self.request.user, flight=flight)


class ReservationRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ReservationRenderer,)
    serializer_class = ReservationSerializer

    queryset = Reservation.objects.all()
    lookup_field = "pk"

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get("pk"),
            flight_id=self.kwargs.get("flight_pk"),
        )
        return obj

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied(
                "You don't have permissions to carry out this action."
            )
        return super().destroy(request, *args, **kwargs)


class CancelReservationAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ReservationRenderer,)
    serializer_class = ReservationSerializer

    queryset = Reservation.objects.all()
    lookup_field = "pk"

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get("pk"),
            flight_id=self.kwargs.get("flight_pk"),
        )
        return obj

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(is_cancelled=True)


@api_view(["GET"])
def flight_reservation_count(request, flight_pk, date, format=None):

    if request.method == "GET":
        queryset = Reservation.objects.filter(
            Q(flight_id=flight_pk) & Q(reserved_at__date=date)
        )
        count = queryset.count()
        content = {"reservations": {"count": count}}
        return Response(content, status=status.HTTP_200_OK)
