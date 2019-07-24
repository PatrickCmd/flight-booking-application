from django.test import TestCase

from authenticate.models import User


class TestUserModel(TestCase):
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
        self.admin_user = User.objects.create_superuser(
            email="test@testadminuser.com",
            password="Testadminuser12344#",
            date_of_birth="1900-11-19",
        )

    def test_user_is_saved(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(self.user.is_active)

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.email)

    def test_user_username(self):
        self.assertEqual(self.user.username, "testuser")

    def test_user_full_name(self):
        self.assertEqual(self.user.get_long_name(), "test user")

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="",
                password="Testuser12344#",
                date_of_birth="1900-11-19",
                username="testuser",
                first_name="test",
                last_name="user",
                gender="m",
                location="testlocation",
                phone="256799000101",
            )

    def test_admin_user(self):
        self.assertTrue(self.admin_user.is_admin)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_verified)
        self.assertTrue(self.admin_user.has_module_perms("authenticate"))
        self.assertTrue(self.admin_user.has_perm("authenticate.delete_user"))
