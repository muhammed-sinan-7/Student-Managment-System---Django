from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.classes.models import Classes
from apps.students.models import Events
# Create your views here.
def std_layout(request):
    return render(request,'students/layout.html')

def profile(request):
    student = request.user.student
    context = {
        'student':student
    }
    return render(request,'students/profile.html',context)

@login_required
def dashboard(request):
    events = Events.objects.all()
    student = request.user.student 
    attendence_percentage = 0
    pending_fees = 0
    upcoming_exam = None
    class_name = None
    if student.class_id:
        class_obj = Classes.objects.filter(class_id=student.class_id).first()
        if class_obj:
            class_name = class_obj.class_name
    context ={
        'student':student,
        'attendence_percentage':attendence_percentage,
        'pending_fees':pending_fees,
        'upcoming_exam':upcoming_exam,
        'class_name':class_name,
        'events':events
    }
    return render(request,'students/dashboard.html',context)

def courses(request):
    return render(request,'students/courses.html')

def attendance(request):
    return render(request,'students/attendences.html')

def fees(request):
    return render(request,'students/fees.html')

def logout(request):
    pass