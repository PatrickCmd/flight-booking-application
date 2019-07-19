# import math

# from django.db.models.signal import post_save, pre_save
# from django.dispatch import receiver

# from .models import Flight, Seat
# from .utils import generate_seats


# @receiver([post_save, pre_save], sender=Flight)
# def create_flight_seats(sender, instance, created, **kwargs):
#     """generate seats whenever a flight is added"""
#     print("Creating flight seats....")
#     if created:
#         seats_per_row = 9
#         row_count = math.ceil(instance.capacity / seats_per_row)
#         generate_seats(Seat, instance, start_row=1, row_count=row_count,
#                        seats_per_row=seats_per_row)
