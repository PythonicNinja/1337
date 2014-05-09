from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class CUser(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'