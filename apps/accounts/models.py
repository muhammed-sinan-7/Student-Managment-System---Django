from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    user_type = models.CharField(
        max_length=20,
        choices=[("student", "Student"),("admin", "Admin"),("teacher", "Teacher")],
        default="student",
    )

    def __str__(self):
        return self.username
