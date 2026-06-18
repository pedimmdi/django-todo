from rest_framework import status
from accounts.tests.base import BaseAPITestCase
from accounts.models import User


class RegisterViewTest(BaseAPITestCase):
    def test_register_success(self):
        payload = {"email": "new@example.com", "password": "password123"}
        response = self.client.post("/api/v1/accounts/register/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="new@example.com").exists())

    def test_register_duplicate_email(self):
        payload = {"email": "test@example.com", "password": "password123"}
        response = self.client.post("/api/v1/accounts/register/", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginViewTest(BaseAPITestCase):
    def test_login_success(self):
        payload = {"email": "test@example.com", "password": "test123456"}
        response = self.client.post("/api/v1/accounts/login/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class ProfileViewTest(BaseAPITestCase):
    def test_profile_requires_authentication(self):
        response = self.client.get("/api/v1/accounts/profile/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile(self):
        self.authenticate()
        response = self.client.get("/api/v1/accounts/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.id)

    def test_update_profile(self):
        self.authenticate()
        payload = {"first_name": "Pedi", "last_name": "Developer", "bio": "Backend Developer"}
        response = self.client.put("/api/v1/accounts/profile/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.first_name, "Pedi")
        self.assertEqual(self.user.profile.last_name, "Developer")
        self.assertEqual(self.user.profile.bio, "Backend Developer")
