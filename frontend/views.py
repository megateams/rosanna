from django.shortcuts import render, redirect, HttpResponse
# from .models import Registration

# # creating views for the registration 
# def save_registration(request):
#     if request.method == 'POST':
#         #Retrieve form data from the request
#         childsurname =request.POST.get('childsurname')
#         childlastname =request.POST.get('childlastname')
        
#         #create a new Registarion object band save it in the database
#         registration =Registration.objects.create(
#             childsurname =childsurname,
#             childlastname =childlastname,
#         )
#         registration.save()
#         return HttpResponse('successful registration')

# Create your views here.
def home(request):
    return render(request,'frontend/dashboard.html')

def login(request):
    return render(request, 'frontend/login.html')

def students(request):
    return render(request, 'frontend/students.html')

# students views
def studentsList(request):
    return render(request, 'frontend/student/studentsList.html')

def studentsAdd(request):
    return render(request, 'frontend/student/studentsAdd.html')


# teachers views
def teacherAdd(request):
    return render(request,'frontend/staff/teacherAdd.html')

def teacherList(request):
    return render(request,'frontend/staff/teacherList.html')
# teachers views

def showStudent(request):
    return render(request, 'frontend/student/showStudent.html')
# students views

# support staff views
def supportstaffAdd(request):
    return render(request, 'frontend/staff/supportstaffAdd.html')

def supportstaffList(request):
    return render(request, 'frontend/staff/supportstaffList.html')

def showSupportstaff(request):
    return render(request, 'frontend/staff/showSupportstaff.html')
# support staff views


def staff(request):
    return render(request, 'frontend/staff.html')
