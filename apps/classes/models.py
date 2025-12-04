from django.db import models

# Create your models here.
class Classes(models.Model):
    class_id = models.CharField(max_length=10)
    class_name = models.CharField(max_length=20)
    class_teacher = models.OneToOneField('teachers.Teacher', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.class_id +" - " + self.class_name + " - " + str(self.class_teacher)