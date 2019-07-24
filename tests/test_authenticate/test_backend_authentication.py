from tests.base_test_case import ProfileBaseTestCase


class TestBackend(ProfileBaseTestCase):
    def test_view_protected_route_with_wrong_token(self):
        self.set_wrong_authorization_header()
        response = self.client.get(self.profile_uri, format="json")
        self.assertEqual(
            response.status_code,
            403,
            "Expected Response Code 403, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn(
            "Invalid authentication. Could not decode token", str(response.data)
        )

    def test_view_protected_route_with_non_existant_user_token(self):
        self.set_no_user_authorization_header()
        response = self.client.get(self.profile_uri, format="json")
        self.assertEqual(
            response.status_code,
            403,
            "Expected Response Code 403, received {0} instead.".format(
                response.status_code
            ),
        )
        self.assertIn("No user matching this token", str(response.data))
