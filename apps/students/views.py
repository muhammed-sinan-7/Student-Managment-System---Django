from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.classes.models import Classes
from apps.students.models import Events
from apps.teachers.models import Notification

# Create your views here.
def std_layout(request):
    return render(request,'students/layout.html')

def profile(request):
    student = request.user.student
    unread_notifications = request.user.notifications.filter(is_read=False).count()
    
    context = {
        'student':student,
        'unread_notifications':unread_notifications
    }
    return render(request,'students/profile.html',context)

@login_required
def dashboard(request):
    events = Events.objects.all()
    student = request.user.student 

    unread_notifications = request.user.notifications.filter(is_read=False).count()
    if student.class_id:
        class_obj = Classes.objects.filter(class_id=student.class_id).first()
        if class_obj:
            class_name = class_obj.class_name
    context ={
        'student':student,
        'events':events,
        'unread_notifications':unread_notifications
    }
    return render(request,'students/dashboard.html',context)

def courses(request):
    student = request.user.student
    
    unread_notifications = request.user.notifications.filter(is_read=False).count()
    

    context = {
        'student': student,
        'unread_notifications':unread_notifications,
    }
    return render(request,'students/courses.html',context)

@login_required
def notifications_view(request):
    
    student = request.user.student
    
    
    notifications = request.user.notifications.all()
    
    
    request.user.notifications.filter(is_read=False).update(is_read=True)
    
    context = {
        'student': student,
        'notifications': notifications,
        'unread_notifications': 0 
    }
    return render(request, 'students/notifications.html', context)
