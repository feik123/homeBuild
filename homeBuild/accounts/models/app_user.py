from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from homeBuild.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    profile_type = models.CharField(
        max_length=20,
        choices=[('homeowner', 'Homeowner'), ('contractor', 'Contractor')],
        default='homeowner'
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    def __str__(self):
        return self.email