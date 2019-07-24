from tests.base_test_case import ReservationBaseTestCase


class TestReservation(ReservationBaseTestCase):
    def test_create_reservation(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        params = {"seat": "A7"}
        response = self.client.post(self.reservation_uri, params, format="json")
        self.assertEqual(
            response.status_code,
            201,
            "Expected Response Code 201, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("test flight", str(response.data))
        self.assertIn("A7", str(response.data))

    def test_create_reservation_with_non_available_seat(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        params = {"seat": "A7"}
        self.client.post(self.reservation_uri, params, format="json")
        res = self.client.post(self.reservation_uri, params, format="json")
        self.assertEqual(
            res.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(res.status_code),
        )
        self.assertIn("Seat is not available", str(res.data))
        self.assertNotIn("A7", str(res.data))

    def test_create_reservation_with_non_existant_seat(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        params = {"seat": "P7"}
        response = self.client.post(self.reservation_uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("Not a valid seat", str(response.data))
        self.assertNotIn("P7", str(response.data))

    def test_view_reservations(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(self.reservation_uri, format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    def test_get_reservation_details(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(
            f"{self.reservation_uri}/{self.reservation.pk}", format="json"
        )
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertNotIn("Entebbe to Denver", str(response.data))
        self.assertIn("test flight", str(response.data))

    def test_get_non_existant_reservation_details(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        pk = 100
        response = self.client.get(f"{self.reservation_uri}/{pk}", format="json")
        self.assertEqual(
            response.status_code,
            404,
            "Expected Response Code 404, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("Not found", str(response.data))

    def test_cancel_reservation(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        response = self.client.patch(
            f"{self.reservation_uri}/{self.reservation.pk}/cancel", format="json"
        )
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertTrue(response.data["is_cancelled"])

    def test_count_flight_reservations_on_given_date(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(
            f"/fbs-api/reservations/{self.flight.pk}/count/{self.reservation.reserved_at.strftime('%Y-%m-%d')}/",  # noqa E501
            format="json",
        )
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertEqual(response.data["reservations"]["count"], 1)
