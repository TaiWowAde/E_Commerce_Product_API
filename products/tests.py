from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory

from categories.models import Category
from .models import Product
from .serializers import ProductSerializer


class ProductModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="owner", password="StrongPass123"
        )
        self.category = Category.objects.create(name="Toys")

    def test_product_creation(self):
        product = Product.objects.create(
            name="Ball",
            description="Round toy",
            price=Decimal("9.99"),
            stock_quantity=5,
            category=self.category,
            created_by=self.user,
        )
        self.assertEqual(str(product), "Ball")
        self.assertEqual(Product.objects.count(), 1)


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="serializer", password="StrongPass123"
        )
        self.category = Category.objects.create(name="Books")

    def test_created_by_from_request(self):
        factory = APIRequestFactory()
        data = {
            "name": "Novel",
            "price": "10.00",
            "stock_quantity": 3,
            "category": self.category.id,
        }
        request = factory.post("/api/products/", data, format="json")
        request.user = self.user

        serializer = ProductSerializer(data=data, context={"request": request})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        product = serializer.save()

        self.assertEqual(product.created_by, self.user)


class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="apiuser", password="StrongPass123"
        )
        self.category = Category.objects.create(name="Electronics")
        self.client.force_authenticate(self.user)

    def test_product_crud_flow(self):
        # Create
        data = {
            "name": "Phone",
            "price": "199.99",
            "stock_quantity": 10,
            "category": self.category.id,
        }
        response = self.client.post("/api/products/", data, format="json")
        self.assertEqual(response.status_code, 201)
        prod_id = response.data["id"]
        self.assertEqual(response.data["created_by"], self.user.id)

        # Retrieve
        response = self.client.get(f"/api/products/{prod_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Phone")

        # Update
        response = self.client.patch(f"/api/products/{prod_id}/", {"stock_quantity": 5}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["stock_quantity"], 5)

        # Delete
        response = self.client.delete(f"/api/products/{prod_id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)



    def test_search_by_category_name(self):
        other_category = Category.objects.create(name="Books")

        Product.objects.create(
            name="Phone",
            description="Smart phone",
            price=Decimal("199.99"),
            stock_quantity=10,
            category=self.category,
            created_by=self.user,
        )
        Product.objects.create(
            name="Novel",
            description="Fiction book",
            price=Decimal("10.00"),
            stock_quantity=5,
            category=other_category,
            created_by=self.user,
        )

        response = self.client.get("/api/products/?search=Electronics")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["name"], "Phone")