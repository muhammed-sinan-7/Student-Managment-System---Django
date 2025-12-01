from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.std_layout, name="regsiter"),
    
]
