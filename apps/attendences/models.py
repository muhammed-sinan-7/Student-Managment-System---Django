from django.db import models
from apps.students.models import Student
# Create your models here.
class Attendences(models.Model):
    att_choices =[
        ('present','Present'),
        ('absent','Absent'),
        ('late','Late'),
        # ('late','Late'),
    ]
    
    student = models.ForeignKey(Student,on_delete=models.CASCADE, blank=True,null=True)
    status = models.CharField(max_length=20,choices=att_choices,blank=True,null=True)
    date = models.DateField()
    
    class Meta:
        unique_together = ['student','date']
        ordering = ['-date']
        
    def __str__(self):
        return self.date + " - " + self.student + ' - ' + self.status