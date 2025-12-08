from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from apps.students.models import Student,Events
from apps.teachers.models import Teacher,Courses
from apps.classes.models import Classes
from apps.teachers.models import Notification



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff']
   
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'user_type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone', 'user_type')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Events)
admin.site.register(Teacher)
admin.site.register(Classes)
admin.site.register(Courses)
admin.site.register(Notification)
