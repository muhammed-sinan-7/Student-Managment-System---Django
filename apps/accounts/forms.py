from django import forms
from .models import CustomUser



class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'placeholder': 'Enter a strong password',
        })
    )

    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control',
            'placeholder': 'Enter email address',
            'name': 'register_email',  
        })
    )

    roll_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Roll Number',
            'autocomplete': 'off',
        }),
        help_text="Required for students",
    )

    teacher_id = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Employee ID',
            'autocomplete': 'off',
        }),
        help_text="Required for teachers",
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'user_type']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'autocomplete': 'off',
                'name': 'register_phone',
            }),
            'user_type': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            if not isinstance(field.widget, forms.HiddenInput):
                field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        
        if self.cleaned_data.get('user_type') == 'admin':
            user.is_staff = True
            user.is_superuser = True
        
        if commit:
            user.save()
        return user

        
class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            'autocomplete': 'off',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'autocomplete': 'off',
        })
    )
