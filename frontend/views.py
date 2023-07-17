from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'frontend/dashboard.html')

def login(request):
    return render(request, 'frontend/login.html')

def studentsList(request):
    return render(request, 'frontend/student/studentsList.html')

def studentsAdd(request):
    return render(request, 'frontend/student/studentsAdd.html')

def staff(request):
    return render(request, 'frontend/staff.html')
