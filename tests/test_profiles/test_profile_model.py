from django.test import TestCase

from authenticate.models import User
from profiles.models import PassportInfo


class TestPassportInfo(TestCase):
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
        self.profile = PassportInfo.objects.create(
            owner=self.user,
            using_country="test country",
            country_of_citizenship="testician",
            passport_number="T373701",
            issue_date="2018-08-08",
            expiration_date="2028-08-08",
        )

    def test_profiles(self):
        self.assertEqual(PassportInfo.objects.count(), 1)

    def test_string_representation(self):
        self.assertEqual(str(self.profile), self.profile.passport_number)
