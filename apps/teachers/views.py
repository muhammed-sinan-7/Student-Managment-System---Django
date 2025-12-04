from django.shortcuts import render
from apps.teachers.models import Teacher
from apps.classes.models import Classes
from apps.students.models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.

def profile(request):
    teacher = Teacher.objects.get(user=request.user)
    assigned_class = Classes.objects.get(class_teacher=teacher)
        
    context = {
        'teacher': teacher,
        'assigned_class': assigned_class,  # Pass full object for template
        'class_name': assigned_class.class_name,
        
    }
    return render(request, "teachers/profile.html", context)
def attendences(request):
    return render(request,'teachers/attendence.html')

def fees(request):
    return render(request,'teachers/fees.html')

@login_required
def students_list(request):
    """Separate view to list all students assigned to the logged-in teacher"""
    
 
    teacher = Teacher.objects.get(user=request.user)
   
    try:
        assigned_class = Classes.objects.get(class_teacher=teacher)
    except Classes.DoesNotExist:
        assigned_class = None
    
    # Get all students assigned to this teacher
    students = Student.objects.filter(teacher=teacher).order_by('roll_number')
    
    context = {
        'teacher': teacher,
        'assigned_class': assigned_class,
        'students': students,
        'total_students': students.count()
    }
    
    return render(request, 'teachers/students_list.html', context)

@login_required
def std_details(request,roll_number):
    student = Student.objects.get(roll_number=roll_number)
    context ={
        'student':student
    }
    return render(request,'teachers/std_detail.html',context)

def student_edit(request,roll_number):
    student = Student.objects.get(roll_number=roll_number)
   
    return render(request,'teachers/std_edit.html')
