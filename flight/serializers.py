from rest_framework import serializers

from .models import Flight, Reservation


class FlightSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.email")

    class Meta:
        model = Flight
        fields = (
            "id",
            "name",
            "origin",
            "destination",
            "departure",
            "arrival",
            "aircraft",
            "status",
            "number",
            "capacity",
            "created_by",
        )


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.first_name")
    flight = serializers.ReadOnlyField(source="flight.name")

    class Meta:
        model = Reservation

        extra_kwargs = {
            "status": {"read_only": True},
            "is_cancelled": {"read_only": True},
            "reserved_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        fields = (
            "id",
            "user",
            "flight",
            "seat",
            "status",
            "is_cancelled",
            "reserved_at",
            "updated_at",
        )
