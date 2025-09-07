from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for viewing and editing products.

    Provides full CRUD functionality with filtering, searching, and
    ordering capabilities. Automatically associates the creating user
    with new products.
    """

    queryset = Product.objects.all().select_related("category", "created_by")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category", "stock_quantity"]
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price", "created_date"]
    ordering = ["-created_date"]

    def perform_create(self, serializer):
        """Attach the requesting user as the product creator."""
        serializer.save(created_by=self.request.user)

