from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Category
from .serializers import CategorySerializer


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Electronics", description="Devices")
        self.assertEqual(str(category), "Electronics")
        self.assertEqual(Category.objects.count(), 1)


class CategorySerializerTest(TestCase):
    def test_serializer_output(self):
        category = Category.objects.create(name="Books")
        serializer = CategorySerializer(category)
        self.assertEqual(serializer.data["name"], "Books")


class CategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="tester", password="StrongPass123"
        )

    def test_category_crud_flow(self):
        self.client.force_authenticate(self.user)

        # Create
        response = self.client.post(
            "/api/categories/", {"name": "Music", "description": "All music"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        cat_id = response.data["id"]

        # Retrieve
        response = self.client.get(f"/api/categories/{cat_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Music")

        # Update
        response = self.client.patch(
            f"/api/categories/{cat_id}/", {"name": "Jazz"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Jazz")

        # Delete
        response = self.client.delete(f"/api/categories/{cat_id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.count(), 0)

