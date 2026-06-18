from django.test import TestCase
from accounts.models import User, Profile


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email="test@example.com", password="test123456")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("test123456"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        user = User.objects.create_superuser(email="admin@example.com", password="admin123456")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
    def test_profile_created_by_signal(self):
        user = User.objects.create_user(email="test@example.com", password="test123456")
        self.assertTrue(Profile.objects.filter(user=user).exists())
    
    def test_user_str(self):
        user = User.objects.create_user(email="test@example.com", password="test123456")
        self.assertEqual(str(user), "test@example.com")

    def test_profile_str(self):
        user = User.objects.create_user(email="test@example.com", password="test123456")
        self.assertEqual(str(user.profile), "test@example.com")
