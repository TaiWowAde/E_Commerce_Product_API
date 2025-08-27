from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from decimal import Decimal

class Category(models.Model):
    """
    id (PK, auto)
    name (unique, max 100, required)
    description (optional)
    created_at (auto)
    updated_at (auto)
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # auto-set on creation
    updated_at = models.DateTimeField(auto_now=True)      # auto-update on modification


    def __str__(self):
        return self.name
