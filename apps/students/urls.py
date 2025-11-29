from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.std_layout, name="home"),
    path("profile", views.profile, name="profile"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("attendance", views.attendance, name="attendance"),
    path("courses", views.courses, name="courses"),
    path("fees", views.fees, name="fees"),
]
