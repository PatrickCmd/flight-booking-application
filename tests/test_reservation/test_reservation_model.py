from django.test import TestCase

from authenticate.models import User
from flight.models import Flight, Reservation


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
        self.reservation = Reservation.objects.create(
            user=self.user, flight=self.flight, seat="A7"
        )

    def test_resewrvation(self):
        self.assertEqual(Reservation.objects.count(), 1)

    def test_string_representation(self):
        self.assertEqual(str(self.reservation), self.flight.name)
