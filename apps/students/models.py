from django.db import models
from apps.accounts.models import CustomUser
from django.conf import settings
from apps.teachers.models import Teacher
from apps.classes.models import Classes
class Student(models.Model):
    
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    roll_number = models.CharField(max_length=10, primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    name = models.CharField(max_length=50)
    class_id = models.CharField(max_length=10, null=True, blank=True)
    class_name = models.CharField(max_length=10,null=True,blank=True)
    dob = models.DateField(null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student',
        null=True,
        blank=True,
    )
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=gender_choices)
    photo = models.ImageField(upload_to='students/', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    father = models.CharField(max_length=30, null=True, blank=True)
    mother_name = models.CharField(max_length=30, null=True, blank=True)
    parent_phone = models.CharField(max_length=15, null=True, blank=True)
    
    def save(self, *args, **kwargs):
       
        if self.teacher:
        # Get the class linked to this teacher (reverse from Classes.class_teacher)
            teacher_class = Classes.objects.filter(class_teacher=self.teacher).first()
            if teacher_class:
                self.class_id = teacher_class.class_id
                self.class_name = teacher_class.class_name
            else:
                self.class_id = None
        else:
            self.class_id = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.name