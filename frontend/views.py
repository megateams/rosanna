from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'frontend/dashboard.html')

def login(request):
    return render(request, 'frontend/login.html')

def students(request):
    return render(request, 'frontend/students.html')
