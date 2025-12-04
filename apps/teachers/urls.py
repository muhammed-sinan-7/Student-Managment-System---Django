from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
   path('profile/',views.profile,name='profile'),
   path('students/',views.students_list,name='students'),
   path('fees/',views.fees,name='fees'),
   path('attendences/',views.attendences,name='attendences'),
   path('student_detail/<str:roll_number>/', views.std_details, name='student_detail'),
   path('student_edit/<str:roll_number>/', views.student_edit, name='student_edit'),

]