from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Manage CRUD operations for product categories.

    Provides list, create, retrieve, update and delete actions. Read-only
    access is granted to unauthenticated users.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

