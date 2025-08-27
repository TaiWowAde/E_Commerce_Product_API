from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator   # <-- add this
from decimal import Decimal                            # <-- and this

from categories.models import Category


class Product(models.Model):
    """
    id (PK, auto)
    name (max 200, required)
    description (optional)
    price (decimal(10,2), required, min 0.01)
    category_id (FK -> Category, required)
    stock_quantity (int, required, min 0)
    image_url (URL, optional)
    created_by_id (FK -> users.User, required)
    created_date (auto)
    updated_date (auto)
    """

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    stock_quantity = models.PositiveIntegerField()  # ≥ 0 by type
    image_url = models.URLField(blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,         # keep products if category is important
        related_name="products",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,         # delete products if owner is removed
        related_name="products",
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        # Helpful indexes for search/filter
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["price"]),
            models.Index(fields=["stock_quantity"]),
            models.Index(fields=["category"]),
            models.Index(fields=["created_by"]),
        ]
        # DB-level safety checks (optional but good)
        constraints = [
            models.CheckConstraint(
                check=models.Q(price__gte=Decimal("0.01")),
                name="price_gte_0_01",
            ),
            models.CheckConstraint(
                check=models.Q(stock_quantity__gte=0),
                name="stock_qty_gte_0",
            ),
        ]
        ordering = ["name"]


    def __str__(self):
        return self.name
