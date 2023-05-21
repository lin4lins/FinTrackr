from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from authorization.managers import CustomUserManager


# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    