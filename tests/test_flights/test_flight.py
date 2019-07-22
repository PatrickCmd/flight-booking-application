from tests.base_test_case import FlightBaseTestCase


class TestFlight(FlightBaseTestCase):
    def test_create_flight(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        params = {
            "name": "Entebbe to Denver",
            "origin": "Entebbe",
            "destination": "Denver",
            "departure": "2019-08-02T08:00:00Z",
            "arrival": "2019-08-03T07:00:00Z",
            "aircraft": "Vintage",
            "status": "ON_TIME",
            "number": "KPQYWT72839",
            "capacity": 120,
        }
        response = self.client.post(self.flight_uri, params, format="json")
        self.assertEqual(
            response.status_code,
            201,
            "Expected Response Code 201, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("Entebbe to Denver", str(response.data))
        self.assertIn("capacity", str(response.data))

    def test_create_flight_when_not_admin_user(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        params = {
            "name": "Entebbe to Denver",
            "origin": "Entebbe",
            "destination": "Denver",
            "departure": "2019-08-02T08:00:00Z",
            "arrival": "2019-08-03T07:00:00Z",
            "aircraft": "Vintage",
            "status": "ON_TIME",
            "number": "KPQYWT72839",
            "capacity": 120,
        }
        response = self.client.post(self.flight_uri, params, format="json")
        self.assertEqual(
            response.status_code,
            403,
            "Expected Response Code 403, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertNotIn("Entebbe to Denver", str(response.data))
        self.assertIn(
            "You don't have permissions to carry out this action.", str(response.data)
        )

    def test_view_flights(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(self.flight_uri, format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    def test_get_flight_details(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(f"{self.flight_uri}{self.flight.pk}", format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertNotIn("Entebbe to Denver", str(response.data))
        self.assertIn("test flight", str(response.data))

    def test_get_non_existant_flight_details(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        pk = 10
        response = self.client.get(f"{self.flight_uri}{pk}", format="json")
        self.assertEqual(
            response.status_code,
            404,
            "Expected Response Code 404, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("Not found", str(response.data))
