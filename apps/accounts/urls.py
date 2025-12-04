from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegView, name="register"),
    path("login/", views.LoginView, name="login"),
    path("logout/", views.Logout, name="logout"),
    
]
