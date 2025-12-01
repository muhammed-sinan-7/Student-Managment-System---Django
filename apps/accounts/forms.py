from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','phone','password','confirm_password','user_type']
        
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields =['username','password']