from django.contrib import admin

from .models import Flight, Seat, Reservation

admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Reservation)
