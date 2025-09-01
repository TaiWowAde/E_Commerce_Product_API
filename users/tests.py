from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .serializers import RegisterSerializer


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@example.com", password="StrongPass123"
        )
        self.assertEqual(str(user), "tester")
        self.assertTrue(user.check_password("StrongPass123"))


class RegisterSerializerTest(TestCase):
    def test_register_serializer_creates_user(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "StrongPass123",
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(user.username, "newuser")


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_and_profile(self):
        # Register new user
        data = {
            "username": "apiuser",
            "email": "apiuser@example.com",
            "password": "StrongPass123",
        }
        response = self.client.post("/api/auth/register/", data, format="json")
        self.assertEqual(response.status_code, 201)

        user = get_user_model().objects.get(username="apiuser")

        # Retrieve profile
        self.client.force_authenticate(user)
        response = self.client.get("/api/users/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "apiuser")

        # Update profile
        response = self.client.patch(
            "/api/users/profile/", {"first_name": "John"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "John")

