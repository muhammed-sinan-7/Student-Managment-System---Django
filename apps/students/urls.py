from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.std_layout, name="home"),
    path("profile", views.profile, name="profile"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('notifications', views.notifications_view, name='notifications'),
    path("courses", views.courses, name="courses"),

]
