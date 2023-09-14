from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import *
from finance.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
import os
from xhtml2pdf import pisa
from django.conf import settings
# Create your views here.

# view for the login page
def login(request):
    return render(request, 'student/login.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Query the database for a student with matching username or studentnumber
        try:
            student = Student.objects.get(username=username)
        except Student.DoesNotExist:
            try:
                student = Student.objects.get(stdnumber=username)
            except Student.DoesNotExist:
                student = None

        if student and student.password == password:
            # If the credentials are valid, redirect to the student dashboard
            request.session['std_number'] = student.stdnumber  # Save the stdnumber in the session
            return redirect('Student Dashboard')  # Replace 'dashboard' with the name/url of your student dashboard view

        else:
            # If the credentials are invalid, display an error message
            messages.error(request, 'Invalid username/studentnumber or password.')
            return redirect('Login Page')
    

def logout_view(request):
    # Clear session data
    request.session.clear()
    # Add a success message to inform the user about the successful logout
    messages.success(request, 'You have been logged out.')
    # Redirect to the login page
    return redirect('Login Page')
# Create your views here.

# dashboard
def dashboard(request):
    # Check if the student is authenticated (if you are using sessions)
    if 'std_number' not in request.session:
        # If the student is not logged in, redirect to the login page
        return redirect('Login Page')  # Replace 'login' with the name/url of your login view

    # Get the studentnumber from the session
    std_number = request.session['std_number']

    student = Student.objects.get(stdnumber=std_number)   
    term_data = Term.objects.all()

    return render(request, 'student/dashboard.html',{'term_data':term_data,'student':student})

# profile
def profile(request,std_number):
    students = Student.objects.get(stdnumber = std_number)
    return render(request, 'student/profile.html',{'student':students})

# Paymentistory
def paymenthistory(request,std_number):
    students = Student.objects.get(stdnumber = std_number)
    fees_list = Fees.objects.filter(stdnumber=std_number)
    return render(request, 'student/paymenthistory.html',{'fees_list':fees_list,'student':students})

