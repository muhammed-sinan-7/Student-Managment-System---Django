# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from apps.teachers.models import Teacher
# from apps.students.models import Student
# from .models import Attendences
# import calendar

# # Create your views here.

# def student_attendence(request):
#     pass
    
    
    
# def teacher_attendence(request):
#     teacher = Teacher.objects.get(user=request.user)
#     students = teacher.students.all()
#     today = timezone.now().date()
#     today_status = {
#         att.student_id: att.status for att in Attendences.objects.filter(student__in=students,date=today)
#     }
    
    