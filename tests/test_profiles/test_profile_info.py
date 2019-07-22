from tests.base_test_case import ProfileBaseTestCase


class TestProfile(ProfileBaseTestCase):
    def test_create_profile(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        params = {
            "using_country": "test country",
            "country_of_citizenship": "testician",
            "passport_number": "T373701",
            "issue_date": "2018-08-08",
            "expiration_date": "2028-08-08",
        }
        response = self.client.post(self.profile_uri, params, format="json")
        self.assertEqual(
            response.status_code,
            201,
            "Expected Response Code 201, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("test country", str(response.data))
        self.assertIn("T373701", str(response.data))

    def test_view_profiles(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(self.profile_uri, content_type="application/json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    def test_get_profile_details(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        response = self.client.get(
            f"{self.profile_uri}{self.profile.pk}/", content_type="application/json"
        )
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("T373701", str(response.data))

    def test_view_all_profiles_when_admin(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {
            "email": "test@testadminuser.com",
            "password": "Testadminuser12344#",
        }
        self.set_authorization_header(login_uri, params_user)
        params = {
            "using_country": "test country",
            "country_of_citizenship": "testician",
            "passport_number": "T373701",
            "issue_date": "2018-08-08",
            "expiration_date": "2028-08-08",
        }
        self.client.post(self.profile_uri, params, format="json")
        response = self.client.get(self.profile_uri, content_type="application/json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertEqual(len(response.data), 2)

    def test_get_non_existant_profile_details(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        pk = 10
        response = self.client.get(
            f"{self.profile_uri}{pk}/", content_type="application/json"
        )
        self.assertEqual(
            response.status_code,
            404,
            "Expected Response Code 404, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("Not found.", str(response.data))
