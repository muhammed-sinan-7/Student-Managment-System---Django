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
    attendence_percentage = 0
    pending_fees = 0
    upcoming_exam = None
    class_name = None
    unread_notifications = request.user.notifications.filter(is_read=False).count()
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
    """Display all notifications for student and mark as read"""
    student = request.user.student
    
    # Get all notifications
    notifications = request.user.notifications.all()
    
    # Mark all as read when page opens
    request.user.notifications.filter(is_read=False).update(is_read=True)
    
    context = {
        'student': student,
        'notifications': notifications,
        'unread_notifications': 0  # ADD THIS LINE - count becomes 0
    }
    return render(request, 'students/notifications.html', context)
