from django.db import models
from apps.accounts.models import CustomUser

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.teacher_id + ' - ' + self.name   