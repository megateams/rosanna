from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import *
from finance.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
import os
from xhtml2pdf import pisa
from django.conf import settings
from django.db.models.functions import Coalesce, Cast
from django.db.models import Avg, F, FloatField 
from frontend.views import encryptpassword

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

        if student and student.password == str(encryptpassword(password)):
            # If the credentials are valid, redirect to the student dashboard
            request.session['std_number'] = student.stdnumber  # Save the stdnumber in the session
            return redirect('Student Dashboard')  # Replace 'dashboard' with the name/url of your student dashboard view

        else:
            # If the credentials are invalid, display an error message
            messages.error(request, 'Invalid username/studentnumber or password. ')
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
    term_data = Term.objects.all().first()

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

def my_results(request, std_number, class_id):
    student = Student.objects.get(stdnumber=std_number)
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    term_data = Term.objects.all()
    mark_types = Mark.MARK_TYPES

    # Get all subjects
    subjects = Subjects.objects.filter(schoolclasses=schoolclass)

    # Initialize a dictionary to store marks for each term, year, and mark type combination
    term_year_marks = {}

    for term in term_data:
        term_marks_data = []
        for mark_type, _ in mark_types:
            # Fetch all marks for the student, class, term, year, and mark type
            marks = Mark.objects.filter(
                class_name=schoolclass,
                student_name=student.childname,
                current_term=term.current_term,
                current_year=term.current_year,
                mark_type=mark_type,
            )

            # Calculate the average mark for each subject within this mark type
            subject_marks = {}
            for mark in marks:
                subject_id = mark.subject.subjectid
                if subject_id not in subject_marks:
                    subject_marks[subject_id] = {
                        'subject_name': mark.subject.subjectname,
                        'total_marks': 0,
                        'marks_count': 0,
                    }
                subject_marks[subject_id]['total_marks'] += mark.marks_obtained
                subject_marks[subject_id]['marks_count'] += 1

            # Calculate average marks for each subject and add to the term_marks_data list
            for subject_id, data in subject_marks.items():
                average_mark = data['total_marks'] / data['marks_count'] if data['marks_count'] > 0 else 0
                term_marks_data.append({
                    'subject_id': subject_id,
                    'subject_name': data['subject_name'],
                    'mark_type': mark_type,
                    'average_mark': average_mark,
                })

        term_year = f"{term.current_term} - {term.current_year}"
        term_year_marks[term_year] = term_marks_data

    context = {
        'student': student,
        'schoolclass': schoolclass,
        'mark_types': mark_types,
        'term_data': term_data,
        'term_year_marks': term_year_marks,
        'subjects': subjects,
    }

    return render(request, 'student/my_results.html', context)

