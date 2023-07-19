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



