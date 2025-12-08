from django.urls import path
from . import views

app_name = "admin_panel"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students/", views.student_list, name="students"),
    path("teachers/", views.teachers, name="teachers"),
    path("courses/", views.courses, name="courses"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/<int:roll_number>/edit/", views.student_edit, name="student_edit"),
    path("students/<int:roll_number>/", views.student_view, name="student_view"),  
    path("students/<int:roll_number>/delete/", views.student_delete, name="student_delete"), 
    path('logout/',views.Logout,name='logout'),
    path("teachers/", views.teachers, name="teachers"),
    path("teachers/add/", views.teacher_add, name="teacher_add"),
    path("teachers/<int:teacher_id>/", views.teacher_view, name="teacher_view"),
    path("teachers/<int:teacher_id>/edit/", views.teacher_edit, name="teacher_edit"),
    path("teachers/<int:teacher_id>/delete/", views.teacher_delete, name="teacher_delete"),
    path("courses/", views.courses, name="courses"),
    path("courses/add/", views.course_add, name="course_add"),
    path("courses/<int:pk>/edit/", views.course_edit, name="course_edit"),
    path("courses/<int:pk>/delete/", views.course_delete, name="course_delete"),
]