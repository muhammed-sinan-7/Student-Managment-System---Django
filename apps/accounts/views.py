from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from apps.students.models import Student
from apps.teachers.models import Teacher
import uuid
# Create your views here.

def home_redirect(request):
    user = request.user

    # If not authenticated at all → go to register
    if not user.is_authenticated:
        return redirect('accounts:register')

    # Ignore superuser and any non-student/teacher user → treat as not logged in
    if user.is_superuser or user.user_type not in ('student', 'teacher'):
        return redirect('accounts:register')

    # If logged in as student → go to student dashboard
    if user.user_type == 'student':
        return redirect('students:dashboard')

    # If logged in as teacher → go to teacher dashboard
    if user.user_type == 'teacher':
        return redirect('teachers:profile')



def RegView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            user_type = form.cleaned_data["user_type"]
            roll_number = form.cleaned_data.get("roll_number")
            teacher_id = form.cleaned_data.get("teacher_id")

            # Auto-generate unique username, e.g. using UUID or email prefix
            def generate_username():
                # Example: use email before @ plus uuid suffix to ensure uniqueness
                prefix = email.split('@')[0]
                return prefix + '_' + uuid.uuid4().hex[:8]

            # Create user but don't commit yet
            user = form.save(commit=False)
            if not user.username:
                user.username = generate_username()
            # You may want to check username uniqueness here or rely on uuid uniqueness
            user.save()

            if user_type == "student":
                if not roll_number:
                    form.add_error(
                        "roll_number",
                        "Roll number is required for student registration.",
                    )
                else:
                    student = Student.objects.filter(roll_number=roll_number).first()
                    if student:
                        student.user = user
                        student.email = email
                        student.phone = phone
                        student.save()
                        return redirect("accounts:login")
                    else:
                        form.add_error(
                            "roll_number",
                            "No student record found with this roll number. Contact admin.",
                        )
            elif user_type == "teacher":
                if not teacher_id:
                    form.add_error(
                        "teacher_id",
                        "Teacher ID is required for teacher registration.",
                    )
                else:
                    teacher = Teacher.objects.filter(teacher_id=teacher_id).first()
                    if teacher:
                        teacher.user = user
                        teacher.email = email
                        teacher.save()
                        return redirect("accounts:login")
                    else:
                        form.add_error(
                            "employee_id",
                            "No teacher record found with this employee ID. Contact admin.",
                        )
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if user.user_type=='student':
                    
                    return redirect("students:dashboard")
                if user.user_type=='teacher':
                    return redirect("teachers:profile")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def Logout(request):
    logout(request)               
    return redirect('accounts:login')  