from tests.base_test_case import BaseTestCase


class TestUserRegistration(BaseTestCase):
    def test_user_registers_successfully(self):
        """
        test user registers successfully
        """
        self.uri = "/fbs-api/users/"
        params = {
            "email": "test1@testuser.com",
            "password": "Testuser12344#",
            "date_of_birth": "1900-11-19",
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "gender": "m",
            "location": "testlocation",
            "phone": "256799000101",
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            201,
            "Expected Response Code 201, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("test1", str(response.data))
        self.assertIn("token", str(response.data))

    def test_already_existing_user(self):
        """
        test user registers already exists
        """
        self.uri = "/fbs-api/users/"
        params = {
            "email": "test@testuser.com",
            "password": "Testuser12344#",
            "date_of_birth": "1900-11-19",
            "username": "testuser",
            "first_name": "test",
            "last_name": "user",
            "gender": "m",
            "location": "testlocation",
            "phone": "256799000101",
        }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn(
            "user with this email address already exists.", str(response.data)
        )

    def test_user_registers_with_empty_fields(self):
        """
        test user registers with empty json fields
        """
        self.uri = "/fbs-api/users/"
        params = {}
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("This field is required.", str(response.data))

    def test_get_logged_in_user_details(self):
        """
        test get logged in user details
        """
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        self.uri = f"/fbs-api/user/{self.test_user.pk}/"

        response = self.client.put(self.uri, format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertEqual("test@testuser.com", str(response.data["email"]))
        self.assertEqual("testuser", str(response.data["username"]))

    def test_user_updates_details(self):
        """
        test user updates bio
        """
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        self.uri = "/fbs-api/user/{self.test_user.pk}/"
        params = {
            "email": "test2@testuser.com",
            "password": "Testuser123445#",
            "date_of_birth": "1900-11-19",
            "username": "testuser2",
            "first_name": "test",
            "last_name": "user",
            "gender": "m",
            "location": "testlocation",
            "phone": "256799000101",
        }
        response = self.client.put(self.uri, params, format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertEqual("test2@testuser.com", str(response.data["email"]))
        self.assertEqual("testuser2", str(response.data["username"]))
