from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration for the custom :class:`User` model in Django admin."""

    list_display = (
        "id",
        "username",
        "email",
        "is_active",
        "is_staff",
        "date_joined",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined")
    ordering = ("id",)
    readonly_fields = ("date_joined", "last_login")

