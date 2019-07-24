import os
from tempfile import TemporaryFile
from unittest.mock import Mock

import cloudinary.uploader

from tests.base_test_case import ProfileBaseTestCase


class TestUploadPassportPhoto(ProfileBaseTestCase):
    def test_upload_image_to_cloudinary_succeeds(self):
        login_uri = "/fbs-api/users/login/"
        params_user = {"email": "test@testuser.com", "password": "Testuser12344#"}
        self.set_authorization_header(login_uri, params_user)
        upload_image_uri = f"{self.profile_uri}{self.profile.pk}/upload_passport_photo"

        cloudinary_mock_response = {
            "public_id": "public_id",
            "secure_url": "http://image_uploaded/here",
        }
        cloudinary.uploader.upload = Mock(
            side_effect=lambda *args: cloudinary_mock_response
        )

        with TemporaryFile() as temp_image_obj:
            for line in open(os.path.dirname(__file__) + "/mock-image.png", "rb"):
                temp_image_obj.write(line)
            response = self.client.post(
                upload_image_uri, {"passport_photo": temp_image_obj}, format="multipart"
            )
            response_data = response.data

            self.assertEqual(
                response.status_code,
                201,
                "Expected Response Code 201, received {0} instead.".format(
                    response.status_code
                ),
            )
            self.assertEqual(response_data["profile"]["status"], "success")
            self.assertEqual(
                response_data["profile"]["photo_data"], cloudinary_mock_response
            )
            self.assertTrue(cloudinary.uploader.upload.called)
