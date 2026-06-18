from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from todo.models import Status, Priority


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user1@test.com", password="password123")
        self.other_user = User.objects.create_user(email="user2@test.com", password="password123")
        self.status = Status.objects.create(name="To Do")
        self.priority = Priority.objects.create(name="High")
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
