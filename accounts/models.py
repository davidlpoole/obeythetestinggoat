import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(models.Model):
    email = models.EmailField(primary_key=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)
