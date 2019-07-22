from django.contrib.auth import get_user_model

from decouple import config
from rest_framework.test import APITestCase, APIClient

from flight.models import Flight, Seat, Reservation
from profiles.models import PassportInfo


class BaseTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = self.setup_user()
        self.test_admin_user = self.setup_admin_user()

    def setup_user(self):
        User = get_user_model()
        user = User.objects.create_user(
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
        return user

    def setup_admin_user(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="test@testadminuser.com",
            password="Testadminuser12344#",
            date_of_birth="1900-11-19",
        )
        return admin_user

    def login_client(self, uri, params):
        response = self.client.post(uri, params, format="json")
        return response

    def set_authorization_header(self, uri, params):
        self.token = self.login_client(uri, params).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT-TOKEN " + self.token)

    def set_wrong_authorization_header(self):
        self.token = "eyey#%@**7372Opdfjdjd"
        self.client.credentials(HTTP_AUTHORIZATION="JWT-TOKEN " + self.token)

    def set_no_user_authorization_header(self):
        self.token = config("NO_USER_TOKEN")
        self.client.credentials(HTTP_AUTHORIZATION="JWT-TOKEN " + self.token)


class ProfileBaseTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.profile = self.setup_profile()
        self.profile_uri = "/fbs-api/profiles/"

    def setup_profile(self):
        profile = PassportInfo.objects.create(
            owner=self.test_user,
            using_country="test country",
            country_of_citizenship="testician",
            passport_number="T373701",
            issue_date="2018-08-08",
            expiration_date="2028-08-08",
        )
        return profile


class FlightBaseTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.flight = self.setup_flight()
        self.seat = self.setup_flight_seat()
        self.flight_uri = "/fbs-api/flights/"

    def setup_flight(self):
        flight = Flight.objects.create(
            name="test flight",
            origin="test origin",
            destination="test destination",
            departure="2019-07-21T23:07:01.841121Z",
            arrival="2019-07-22T23:07:01.841121Z",
            aircraft="KLM",
            status="ON_TIME",
            created_by=self.test_admin_user,
            number="KL8190",
            capacity=120,
        )
        return flight

    def setup_flight_seat(self):
        seat = Seat.objects.create(
            seat_number="A7", flight=self.flight, is_available=True
        )
        return seat


class ReservationBaseTestCase(FlightBaseTestCase):
    def setUp(self):
        super().setUp()
        self.reservation = self.setup_reservation()
        self.reservation_uri = f"/fbs-api/flights/{self.flight.pk}/reservations"

    def setup_reservation(self):
        reservation = Reservation.objects.create(
            user=self.test_user, flight=self.flight, seat="A7"
        )
        return reservation
