from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    bio = models.CharField(max_length=100)
    avatar = models.ImageField(
            upload_to='users/avatars/%Y/%m/%d/',
            default='users/avatars/default.jpg'
        )
