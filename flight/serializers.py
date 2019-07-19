from rest_framework import serializers

from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Flight
        fields = ('id', 'name', 'origin', 'destination', 'departure', 'arrival',
                  'aircraft', 'status', 'number', 'capacity', 'created_by',)
