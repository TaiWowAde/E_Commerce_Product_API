from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock_quantity", "category", "created_by", "created_date")
    list_filter  = ("category",)
    search_fields = ("name",)
