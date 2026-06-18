from django.test import TestCase
from accounts.api.v1.serializers import (UserRegistrationSerializer, ProfileSerializer)
from accounts.models import User


class UserRegistrationSerializerTest(TestCase):
    def test_valid_data(self):
        payload = {"email": "test@example.com", "password": "test123456"}
        serializer = UserRegistrationSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        
    def test_create_user(self):
        payload = {"email": "test@example.com", "password": "test123456"}
        serializer = UserRegistrationSerializer(data=payload)
        serializer.is_valid()
        user = serializer.save()
        self.assertEqual(user.email, payload["email"])


class ProfileSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="test123456")

    def test_profile_serializer(self):
        serializer = ProfileSerializer(self.user.profile)
        self.assertEqual(serializer.data["user"], self.user.id)
