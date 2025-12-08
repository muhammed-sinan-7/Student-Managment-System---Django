from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import logout
from apps.students.models import Student
from apps.teachers.models import Teacher, Courses


def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_courses': Courses.objects.count(),
        'upcoming_events': 5,
    }
    return render(request, 'admin_panel/dashboard.html', context)


def students(request):
    students = Student.objects.all().order_by('-roll_number')
    return render(request, 'admin_panel/students.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        try:
            student = Student(
                roll_number=request.POST.get('roll_number'),
                name=request.POST.get('name'),
                teacher_id=request.POST.get('teacher') if request.POST.get('teacher') else None,
                class_id=request.POST.get('class_id'),
                class_name=request.POST.get('class_name'),
                dob=request.POST.get('dob') or None,
                email=request.POST.get('email') or None,
                gender=request.POST.get('gender') or None,
                phone=request.POST.get('phone') or None,
                father=request.POST.get('father') or None,
                mother_name=request.POST.get('mother_name') or None,
                parent_phone=request.POST.get('parent_phone') or None,
            )
            if request.FILES.get('photo'):
                student.photo = request.FILES['photo']
            student.save()
            messages.success(request, f'Student {student.name} added successfully!')
            return redirect('admin_panel:students')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    teachers_list = Teacher.objects.all()
    return render(request, 'admin_panel/student_add.html', {'teachers': teachers_list})

def student_view(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    return render(request, 'admin_panel/student_view.html', {'student': student})

def student_edit(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    teachers_list = Teacher.objects.all()
    
    if request.method == 'POST':
        try:
            student.name = request.POST.get('name') or student.name
            student.teacher_id = request.POST.get('teacher') if request.POST.get('teacher') else student.teacher_id
            student.class_id = request.POST.get('class_id') or student.class_id
            student.class_name = request.POST.get('class_name') or student.class_name
            student.dob = request.POST.get('dob') or student.dob
            student.email = request.POST.get('email') or student.email
            student.gender = request.POST.get('gender') or student.gender
            student.phone = request.POST.get('phone') or student.phone
            student.father = request.POST.get('father') or student.father
            student.mother_name = request.POST.get('mother_name') or student.mother_name
            student.parent_phone = request.POST.get('parent_phone') or student.parent_phone
            
            if request.FILES.get('photo'):
                student.photo = request.FILES['photo']
            student.save()
            messages.success(request, f'{student.name} updated successfully!')
            return redirect('admin_panel:student_view', roll_number=student.roll_number)
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'admin_panel/student_edit.html', {
        'student': student, 
        'teachers': teachers_list
    })

def student_delete(request, roll_number):
    if request.method == 'POST':
        student = get_object_or_404(Student, roll_number=roll_number)
        student_name = student.name
        student.delete()
        messages.success(request, f'Student "{student_name}" deleted successfully!')
        return redirect('admin_panel:students')


def student_list(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.all().order_by('roll_number')  
    
    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(roll_number__icontains=query) |
            Q(email__icontains=query)
        ).distinct()
    
    context = {
        'students': students,
        'query': query,
        'count': students.count(),
    }
    return render(request, 'admin_panel/students.html', context)
def teachers(request):
    teachers_list = Teacher.objects.prefetch_related('students').order_by('name')
    return render(request, 'admin_panel/staffs.html', {'teachers': teachers_list})

def teacher_add(request):
    if request.method == 'POST':
        try:
            teacher = Teacher(
                teacher_id=request.POST.get('teacher_id'),
                name=request.POST.get('name'),
                email=request.POST.get('email'),
            )
            teacher.save()
            messages.success(request, f'Teacher {teacher.name} (ID: {teacher.teacher_id}) added successfully!')
            return redirect('admin_panel:teachers')
        except Exception as e:
            messages.error(request, f'Error adding teacher: {str(e)}')
    return render(request, 'admin_panel/teacher_add.html')

def teacher_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    return render(request, 'admin_panel/teacher_view.html', {'teacher': teacher})

def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    
    if request.method == 'POST':
        try:
            teacher.teacher_id = request.POST.get('teacher_id') or teacher.teacher_id
            teacher.name = request.POST.get('name')
            teacher.email = request.POST.get('email')
            teacher.save()
            messages.success(request, f'Teacher {teacher.name} updated successfully!')
            return redirect('admin_panel:teachers')
        except Exception as e:
            messages.error(request, f'Error updating teacher: {str(e)}')
    
    return render(request, 'admin_panel/teacher_edit.html', {'teacher': teacher})
def teacher_delete(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
        teacher_name = teacher.name
        teacher.delete()
        messages.success(request, f'{teacher_name} deleted successfully!')
        return redirect('admin_panel:teachers')
   


def courses(request):
    courses_list = Courses.objects.prefetch_related('students').order_by('name')
    return render(request, 'admin_panel/courses.html', {'courses': courses_list})

def course_add(request):
    if request.method == 'POST':
        try:
            
            fees_value = request.POST.get('fees')  
            fees = float(fees_value) if fees_value else 0.00
            
            course = Courses(
                name=request.POST.get('name'),
                course_id=request.POST.get('course_id'),  
                description=request.POST.get('description') or None,
                duration=int(request.POST.get('duration')) if request.POST.get('duration') else None,
                fees=fees,  
            )
            
            
            if request.FILES.get('image'):
                course.image = request.FILES['image']
                
            course.save()
            messages.success(request, f'Course "{course.name}" (ID: {course.course_id}) added successfully!')
            return redirect('admin_panel:courses')
            
        except ValueError as e:
            messages.error(request, f'Invalid number format: {str(e)}')
        except Exception as e:
            messages.error(request, f'Error adding course: {str(e)}')
    
    return render(request, 'admin_panel/course_add.html')

def course_edit(request, pk):
    course = get_object_or_404(Courses, id=pk)
    if request.method == 'POST':
        try:
            course.name = request.POST.get('name')
            course.duration = request.POST.get('duration')
            course.fee = request.POST.get('fee')
            course.description = request.POST.get('description')
            course.save()
            messages.success(request, f'Course {course.name} updated successfully!')
            return redirect('admin_panel:course_view', pk=course.id)
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    return render(request, 'admin_panel/course_edit.html', {'course': course})

def course_delete(request, pk):
    course = get_object_or_404(Courses, id=pk)
    if request.method == 'POST':
        course_name = course.name
        course.delete()
        messages.success(request, f'{course_name} deleted successfully!')
        return redirect('admin_panel:courses')
    return render(request, 'admin_panel/course_delete.html', {'course': course})


def Logout(request):
    logout(request)
    return redirect('accounts:login')