from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from users.managers import CustomUserManager
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length= 15)
    
    USERNAME_FIELD = "email"  # Use email instead for user
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    