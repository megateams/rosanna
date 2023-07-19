from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
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

# Send the registration staff details to and retrieve from database 
def supportstaffreg(request):
    # retrieve data from request
    if request.method == 'POST':
        fullname =request.POST.get('fullname')
        contact =request.POST.get('contact')
        email =request.POST.get('email')
        address =request.POST.get('address')
        gender =request.POST.get('gender')
        dob =request.POST.get('dob')
        qualification =request.POST.get('qualification')
        position =request.POST.get('position')
        
        #create support staff object and submit it in the database
        supportStaffReg =Supportstaff.objects.create(
            fullname =fullname,
            contact=contact,
            email=email,
            address=address,
            gender=gender,
            dob=dob,
            qualification=qualification,
            position=position            
        )
        supportStaffReg.save()
        messages.success(request, f" Your data, {fullname} has been successfully added!")
                
        # Redirect to the registration page for support staff after successful data addition
        return redirect('AddSupportstaff')
   
def supportstaffList(request):
    # Retrieve all support staff data from the database
    all_support_staff = Supportstaff.objects.all()
    # Pass the data to the template for rendering
    return render(request, 'frontend/staff/supportstaffList.html', {'support_staff': all_support_staff})
    
def showSupportstaff(request):
    return render(request, 'frontend/staff/showSupportstaff.html')
# support staff views

def staff(request):
    return render(request, 'frontend/staff.html')


