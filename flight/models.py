from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Flight(models.Model):
    STATUSES = (
        ('DELAYED', 'DELAYED'),
        ('ON_TIME', 'ON_TIME'),
        ('ARRIVED', 'ARRIVED'),
        ('LATE', 'LATE'),
    )

    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    aircraft = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUSES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='flights',
                                   on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
    
    @property
    def seats(self):
        return self.seats.objects.all()


class Seat(models.Model):
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    flight = models.ForeignKey(Flight, related_name='seats',
                               on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.flight}_{self.flight.number}-{self.seat_number}"


class Reservation(models.Model):
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('CANCELLED', 'CANCELLED'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reservations',
                             on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='reservations', on_delete=models.CASCADE)
    seat = models.CharField(max_length=5, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='ACTIVE')
    is_cancelled = models.BooleanField(default=False)
    reserved_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.flight.name