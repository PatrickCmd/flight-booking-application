from tests.base_test_case import BaseTestCase


class TestUserLogin(BaseTestCase):
    def test_user_logins_successfully(self):
        """
        test user logins successfully
        """
        self.uri = "/fbs-api/users/login/"
        params = {"email": "test@testuser.com", "password": "Testuser12344#"}
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("test", str(response.data))
        self.assertIn("token", str(response.data))

    def test_user_logins_with_wrong_email(self):
        """
        test user logins with wrong email
        """
        self.uri = "/fbs-api/users/login/"
        params = {"email": "test1@testuser.com", "password": "Testuser12344#"}
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn(
            "A user with this email and password was not found.", str(response.data)
        )

    def test_user_logins_with_empty_email(self):
        """
        test user logins with wrong email
        """
        self.uri = "/fbs-api/users/login/"
        params = {"email": "", "password": "Testuser12344#"}
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("An email address is required to log in.", str(response.data))

    def test_user_logins_with_wrong_password(self):
        """
        test user logins with wrong password
        """
        self.uri = "/fbs-api/users/login/"
        params = {"email": "test@testuser.com", "password": "Testuser12345#"}
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn(
            "A user with this email and password was not found.", str(response.data)
        )

    def test_user_logins_with_empty_password(self):
        """
        test user logins with wrong email
        """
        self.uri = "/fbs-api/users/login/"
        params = {"email": "test@testuser.com", "password": ""}
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("A password is required to log in.", str(response.data))
