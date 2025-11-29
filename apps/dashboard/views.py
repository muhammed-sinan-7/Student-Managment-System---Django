from django.shortcuts import render

def student_dash(request):
    return render(request, 'dashboard/student_dash.html')
