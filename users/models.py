from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Matches ERD:
    id (PK, auto) — provided by Django
    username (unique, max 150, required) — provided by AbstractUser
    email (unique, required) — we enforce uniqueness
    password (hashed) — handled by Django user manager
    first_name (max 30, optional) — we reduce max length to 30
    last_name (max 30, optional) — we reduce max length to 30
    is_active (default True) — provided by AbstractUser
    date_joined (auto-set) — provided by AbstractUser
    """

    # Make email unique (and effectively required at serializer/form level)
    email = models.EmailField(unique=True)

    # Override lengths to match ERD (optional; Django’s defaults are 150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name  = models.CharField(max_length=30, blank=True)

    # username, password, is_active, date_joined remain from AbstractUser

    def __str__(self):
        return self.username

#Notes
#Passwords are hashed automatically via create_user() / DRF serializers.
#date_joined is set automatically by Django (functionally same as “auto-set on creation”)
#This uses Django’s built-ins for: id (PK), username (unique), password (hashed), is_active, date_joined.