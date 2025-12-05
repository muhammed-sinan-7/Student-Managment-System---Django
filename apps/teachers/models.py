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
    
    
class Courses(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    course_id = models.CharField(max_length=10,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    duration = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='courses/',null=True,blank=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='notifications')
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    message = models.TextField()
    title = models.CharField(max_length=50,null=True,blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.recipient.email} - {self.title}'