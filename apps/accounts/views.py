from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def RegView(request):
    # frm = RegisterForm()
    if request.method == 'POST':
        frm = RegisterForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('login')
    else:
        frm = RegisterForm()
    return render(request,'register.html',{'frm':frm})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, "Login Succefully")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials..!")
            
    return render(request,'accounts/login.html')