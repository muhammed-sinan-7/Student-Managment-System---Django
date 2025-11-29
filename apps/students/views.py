from django.shortcuts import render

# Create your views here.
def std_layout(request):
    return render(request,'students/layout.html')

def profile(request):
    return render(request,'profile.html')

def dashboard(request):
    return render(request,'dashboard.html')

def courses(request):
    return render(request,'courses.html')

def attendance(request):
    return render(request,'attendences.html')

def fees(request):
    return render(request,'fees.html')