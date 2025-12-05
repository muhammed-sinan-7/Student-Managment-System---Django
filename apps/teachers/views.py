from django.shortcuts import render,get_object_or_404,redirect
from apps.teachers.models import Teacher
from apps.classes.models import Classes
from apps.students.models import Student
from django.contrib.auth.decorators import login_required
from apps.teachers.models import Courses,Notification
from django.contrib import messages
from apps.accounts.models import CustomUser
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
    all_courses = Courses.objects.all()
    context ={
        'student':student,
        'all_course':all_courses
    }
    return render(request,'teachers/std_detail.html',context)

def student_edit(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.class_id = request.POST.get('class_id') or None
        student.class_name = request.POST.get('class_name') or None
        student.dob = request.POST.get('dob') or None
        student.email = request.POST.get('email') or None
        student.gender = request.POST.get('gender') or None
        student.phone = request.POST.get('phone') or None
        student.father = request.POST.get('father') or None
        student.mother_name = request.POST.get('mother_name') or None
        student.parent_phone = request.POST.get('parent_phone') or None
        
      
        course_ids = request.POST.getlist('courses')  
        if course_ids:
            student.courses.set(course_ids)
        else:
            student.courses.clear()
            
        
        if request.FILES.get('photo'):
            student.photo = request.FILES['photo']
            
        student.save()
        
        messages.success(request, f'Student {student.name} updated successfully!')
        return redirect('teachers:student_detail', roll_number=roll_number) 
        
    context = {
        'student': student,
        'courses': Courses.objects.all(),
    }
    return render(request, 'teachers/std_edit.html', context)
   
    
def add_course(request,roll_number):
    course_id = request.POST.get('course_id')
    student = get_object_or_404(Student, roll_number=roll_number)
    course = get_object_or_404(Courses, course_id=course_id)
    student.course = course
    student.save()
    
    Notification.objects.create(
        recipient = student.user,
        sender = request.user,
        title='New Course Assigned',
        message =f'You have been enrolled in {course.name} course by your teacher.'
    )
    
    messages.success(request,f'Course assigned to {student.name}!')
    return redirect('teachers:student_detail' , roll_number=roll_number)


