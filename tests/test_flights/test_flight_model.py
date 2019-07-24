from django.test import TestCase

from authenticate.models import User
from flight.models import Flight, Seat


class TestFlight(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@testuser.com",
            password="Testuser12344#",
            date_of_birth="1900-11-19",
            username="testuser",
            first_name="test",
            last_name="user",
            gender="m",
            location="testlocation",
            phone="256799000101",
        )
        self.flight = Flight.objects.create(
            name="test flight",
            origin="test origin",
            destination="test destination",
            departure="2019-07-21T23:07:01.841121Z",
            arrival="2019-07-22T23:07:01.841121Z",
            aircraft="KLM",
            status="ON_TIME",
            created_by=self.user,
            number="KL8190",
            capacity=120,
        )
        self.seat = Seat.objects.create(
            seat_number="A7", flight=self.flight, is_available=True
        )

    def test_flight(self):
        self.assertEqual(Flight.objects.count(), 1)

    def test_string_representation(self):
        self.assertEqual(str(self.flight), self.flight.name)

    def test_flight_seats(self):
        self.assertEqual(self.flight.seats.count(), 1)
        self.assertEqual(len(self.flight.flight_seats), 1)

    def test_seat_string_representation(self):
        self.assertEqual(
            str(self.seat),
            f"{self.flight}_{self.flight.number}_{self.seat.seat_number}",
        )

    def test_seat(self):
        self.assertEqual(Seat.objects.count(), 1)
