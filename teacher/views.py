from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
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
    return render(request, 'teacher/login.html')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Query the database for a teacher with matching username or email
        try:
            teacher = Teachers.objects.get(username=username)
        except Teachers.DoesNotExist:
            try:
                teacher = Teachers.objects.get(email=username)
            except Teachers.DoesNotExist:
                teacher = None

        if teacher and teacher.password == password:
            # If the credentials are valid, redirect to the teacher dashboard
            request.session['teacher_id'] = teacher.teacherid  # Save the teacher's ID in the session
            return redirect('Teacher Dashboard')  # Replace 'dashboard' with the name/url of your teacher dashboard view

        else:
            # If the credentials are invalid, display an error message
            messages.error(request, 'Invalid username/email or password.')
            return redirect('Login Page')
    

def logout_view(request):
    # Clear session data
    request.session.clear()
    # Add a success message to inform the user about the successful logout
    messages.success(request, 'You have been logged out.')
    # Redirect to the login page
    return redirect('Login Page')

def dashboard(request):
    # Check if the teacher is authenticated (if you are using sessions)
    if 'teacher_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('Login Page')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    teacher_id = request.session['teacher_id']

    teacher = Teachers.objects.get(teacherid=teacher_id)    
    term_data = Term.objects.all()
    return render(request, 'teacher/dashboard.html',{'teacher': teacher, 'term_data':term_data})

def profile(request,teacher_id):
    teachers = Teachers.objects.get(teacherid = teacher_id)
    return render(request, 'teacher/profile.html', {'teacher': teachers})    


def paymenthistory(request,teacher_id):
    teachers = Teachers.objects.get(teacherid = teacher_id)
    teacher_data = Teacherspayment.objects.filter(teacherid=teacher_id)
    return render(request, 'teacher/paymenthistory.html', {"teacher_data": teacher_data, 'teacher':teachers})   

# marks logic
def get_students_by_class(request, class_id):
    try:
        selected_class = Schoolclasses.objects.get(pk=class_id)
        students = Student.objects.filter(stdclass=selected_class)
        data = {
            'students': list(students.values('pk', 'childname')),
            # Add other fields you want to include in the JSON response
        }
        return JsonResponse(data)
    except Schoolclasses.DoesNotExist:
        data = {'error': 'Class not found'}
        return JsonResponse(data, status=404)

def get_subjects(request, class_id):
    class_obj = get_object_or_404(Schoolclasses, pk=class_id)
    subjects = class_obj.subjects.all().values('subjectid', 'subjectname')
    return JsonResponse(list(subjects), safe=False)


# views.py
from django.db.models import Sum

def class_details(request, class_id, teacher_id):
    # Retrieve the class and teacher objects based on the provided IDs
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)

    # Get the students for this class taught by the teacher
    students = Student.objects.filter(stdclass=schoolclass)

    # Get the subjects taught by the teacher for this class
    subjects = teacher.subjects.filter(schoolclasses=schoolclass)

    mark_types = Mark.MARK_TYPES
    # Create a dictionary to hold the marks for each student and subject combination
    student_marks = {}
    for student in students:
        student_marks[student] = {}
        for subject in subjects:
            marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, subject=subject)
            student_marks[student][subject] = {mark.mark_type: mark.marks_obtained for mark in marks}

    # Calculate average marks for each subject for each student
    for student, subject_marks in student_marks.items():
        for subject, mark_dict in subject_marks.items():
            bot_marks = mark_dict.get('BOT', 0)
            mot_marks = mark_dict.get('MOT', 0)
            eot_marks = mark_dict.get('EOT', 0)

            total_marks = bot_marks + mot_marks + eot_marks
            total_mark_entries = len(mark_dict)
            average_marks = total_marks / total_mark_entries if total_mark_entries > 0 else 0

            student_marks[student][subject]['average_marks'] = average_marks

    return render(request, 'teacher/class_details.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'student_marks': student_marks,
        'mark_types': mark_types,
        'term_data': Term.objects.all()
    })



# views.py
def class_marks_by_marktype(request, class_id, teacher_id):
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    teacher = Teachers.objects.get(teacherid=teacher_id)
    mark_type = request.GET.get('marktype')  # Get the mark type from the query parameter
    
    students = Student.objects.filter(stdclass=schoolclass)
    subjects = teacher.subjects.filter(schoolclasses=schoolclass)
    mark_types = Mark.MARK_TYPES
    student_marks = {}
    for student in students:
        marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, mark_type=mark_type)
        student_marks[student] = {subject: marks.filter(subject=subject).first() for subject in subjects}

    # Calculate total marks and average marks for each student
    for student, marks_dict in student_marks.items():
        total_marks = 0
        total_subjects = 0
        for marks in marks_dict.values():
            if marks:
                total_marks += marks.marks_obtained
                total_subjects += 1
        if total_subjects > 0:
            student.total_marks = total_marks
            student.average_marks = total_marks / total_subjects
        else:
            student.total_marks = 0
            student.average_marks = 0
    return render(request, 'teacher/result_details.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'student_marks': student_marks,
        'mark_types' :mark_types,
        'mark_type' :mark_type,
    })

# from django.shortcuts import get_object_or_404

def addsubjectmarks(request, class_id, teacher_id, subject_id):
    # Check if the teacher is authenticated (if you are using sessions)
    if 'teacher_id' not in request.session or request.session['teacher_id'] != teacher_id:
        # If the teacher is not logged in or the session teacher_id doesn't match, redirect to the login page
        return redirect('login')  # Replace 'login' with the name/url of your login view

    # Retrieve the class and subject objects
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    subject = get_object_or_404(Subjects, subjectid=subject_id)

    # Retrieve the students related to the class
    students = Student.objects.filter(stdclass=schoolclass)
    # Retrieve the mark types for the dropdown
    mark_types = Mark.MARK_TYPES

    term_data = Term.objects.all().first()
    # Get the marks for the current subject
    marks = Mark.objects.filter(class_name=schoolclass, subject=subject)

    # Create a set of student names whose marks have been added for the current subject
    marks_students = set(mark.student_name for mark in marks)
    
    # Handle form submission to add subject marks
    if request.method == 'POST':
        mark_type = request.POST.get('marktype')
        student_number = request.POST.get('studentname')
        marks_obtained = request.POST.get('mark_obtained')

        if mark_type and student_number and marks_obtained:
            # Get the student object
            student = Student.objects.get(stdnumber=student_number)

            # Check if a mark of the same type already exists for the student and subject
            existing_mark = Mark.objects.filter(
                class_name=schoolclass,
                student_name=student.childname,
                subject=subject,
                mark_type=mark_type,
                current_term=term_data.current_term,
                current_year=term_data.current_year,
            ).first()

            if existing_mark:
                # If a mark already exists, update it
                existing_mark.marks_obtained = int(marks_obtained)
                existing_mark.save()
                messages.success(request, 'Subject mark updated successfully.')
            else:
                # If a mark doesn't exist, create a new one
                mark = Mark.objects.create(
                    class_name=schoolclass,
                    student_name=student.childname,
                    subject=subject,
                    marks_obtained=int(marks_obtained),
                    mark_type=mark_type,
                    current_term=term_data.current_term,
                    current_year=term_data.current_year,
                )
                mark.save()
                messages.success(request, 'Subject mark added successfully.')

            return redirect('Add Subject marks', class_id=class_id, teacher_id=teacher_id, subject_id=subject_id)

    return render(request, 'teacher/marks/add_subject_marks.html', {
        'schoolclass': schoolclass,
        'subject': subject,
        'students': students,
        'mark_types': mark_types,
        'marks_students': marks_students,
        'teacher_id': teacher_id,
        'term_data': term_data,
    })

def addmarks(request, class_id, teacher_id):
    # Check if the teacher is authenticated (if you are using sessions)
    if 'teacher_id' not in request.session or request.session['teacher_id'] != teacher_id:
        # If the teacher is not logged in or the session teacher_id doesn't match, redirect to the login page
        return redirect('login')  # Replace 'login' with the name/url of your login view

    # Retrieve the class object
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)

    # Retrieve the students related to the class
    students = Student.objects.filter(stdclass=schoolclass)

    # Retrieve the subjects that are associated with this class
    subjects = schoolclass.subjects.all()

    # getting the current term data
    term_data = Term.objects.all().first()

    # Retrieve the mark types for the dropdown
    mark_types = Mark.MARK_TYPES

    marktype = request.GET.get('marktype')
    # Handle form submission to add subject marks
    if request.method == 'POST':
        mark_type = request.POST.get('marktype')
        student_number = request.POST.get('studentname')
        marks_obtained = request.POST.get('mark_obtained')
        subject_id = request.POST.get('subject')

        # Check if the mark already exists for the given student, mark type, and subject
        if Mark.objects.filter(class_name=schoolclass, student_name=student_number, subject_id=subject_id, mark_type=mark_type).exists():
            messages.error(request, 'Mark already added for this student')
        else:
            # Create a new Mark object to save the marks
            Mark.objects.create(
                class_name=schoolclass,
                student_name=student_number,
                subject_id=subject_id,
                mark_type=mark_type,
                marks_obtained=int(marks_obtained),
                current_term=term_data.current_term,
                current_year=term_data.current_year,
            )
            messages.success(request, 'Subject marks added successfully.')

        return redirect('Add Marks', class_id=class_id, teacher_id=teacher_id)

    # If the request method is GET, render the form for adding subject marks
    return render(request, 'teacher/marks/addMarks.html', {
        'schoolclass': schoolclass,
        'subjects': subjects,
        'mark_types': mark_types,
        'teacher_id': teacher_id,
        'students': students,
        'marktype': marktype,
        'term_data': term_data,
    })

# view to check if the mark already exists
def get_mark(request, student_id, subject_id, mark_type):
    # Retrieve the mark for the specified student, subject, and mark type
    
    mark = Mark.objects.filter(
        student_name=student_id,
        subject=subject_id,
        mark_type=mark_type
    ).first()
    print(mark)
    # Prepare the response data
    response_data = {'marks_obtained': mark.marks_obtained if mark else ''}

    return JsonResponse(response_data)

# class teacher class
def his_class(request, class_id, teacher_id):
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)

    # Get the students for this class taught by the teacher
    students = Student.objects.filter(stdclass=schoolclass)

    # Get the subjects taught by the teacher for this class
    subjects = Subjects.objects.filter(schoolclasses=schoolclass)

    # Get the teachers who teach that class
    teachers_in_class = Teachers.objects.filter(classes=schoolclass)
    # print (teachers_in_class)
    # Calculate the number of boys and girls in the class
    num_boys = students.filter(gender='m').count()
    num_girls = students.filter(gender='f').count()

    # Create a dictionary to hold the marks for each student and subject combination
    student_marks = {}
    for student in students:
        marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname)
        student_marks[student] = {subject: marks.filter(subject=subject).first() for subject in subjects}
    
    term_data = Term.objects.all()

    return render(request, 'teacher/his_class.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'student_marks': student_marks,
        'teachers_in_class': teachers_in_class,
        'num_girls': num_girls,
        'num_boys': num_boys,
        'term_data': term_data,
    })

# view marks


def view_marks(request, class_id, teacher_id):
    # Retrieve the class and teacher objects based on the provided IDs
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)

    # Get the students for this class taught by the teacher
    students = Student.objects.filter(stdclass=schoolclass)

    # Get all subjects
    subjects = Subjects.objects.filter(schoolclasses=schoolclass)
    subjects_count = Subjects.objects.filter(schoolclasses=schoolclass).count()

    mark_types = Mark.MARK_TYPES
    term_data = Term.objects.all()
    # Create a dictionary to hold the total and average marks for each subject for each student
    subjects_marks_data = {}
    subjects_total_marks = {subject: 0 for subject in subjects}
    subjects_marks_count = {subject: 0 for subject in subjects}

    for student in students:
        student_subjects_data = []
        total_average_marks = 0  # Initialize total_average_marks for each student
        for subject in subjects:
            total_marks = 0
            marks_count = 0
            marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, subject=subject)
            for mark in marks:
                total_marks += mark.marks_obtained
                marks_count += 1
                subjects_total_marks[subject] += mark.marks_obtained
                subjects_marks_count[subject] += 1

            average_marks = total_marks / marks_count if marks_count > 0 else 0
            total_average_marks += average_marks
            final_average = total_average_marks / subjects_count if marks_count > 0 else 0
              # Accumulate average marks for the student
            student_subjects_data.append({
                'subject': subject,
                'total_marks': total_marks,
                'average_marks': average_marks,
            })

        subjects_marks_data[student] = student_subjects_data
        student.total_average_marks = total_average_marks  # Store total average marks for the student
        student.final_average = final_average
        # Calculate average marks for each subject across all students
        subjects_average_marks = {subject: total_marks / marks_count if marks_count > 0 else 0
                                for subject, total_marks in subjects_total_marks.items()}
        # Sort the students based on their final average marks in descending order
        # students = sorted(students, key=lambda student: student.final_average, reverse=True)

    # Assign ranks to students based on their position in the sorted list
    for rank, student in enumerate(students, start=1):
        student.rank = rank
    return render(request, 'teacher/marks/view_all_marks.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'mark_types': mark_types,
        'subjects_marks_data': subjects_marks_data,
        'term_data': term_data
    })



# views.py
def view_marks_by_marktype(request, class_id, teacher_id):
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    teacher = Teachers.objects.get(teacherid=teacher_id)
    mark_type = request.GET.get('marktype')  # Get the mark type from the query parameter
    
    students = Student.objects.filter(stdclass=schoolclass)
    subjects = Subjects.objects.filter(schoolclasses=schoolclass)
    mark_types = Mark.MARK_TYPES
    student_marks = {}
    for student in students:
        marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, mark_type=mark_type)
        student_marks[student] = {subject: marks.filter(subject=subject).first() for subject in subjects}

    # Calculate total marks and average marks for each student
    for student, marks_dict in student_marks.items():
        total_marks = 0
        total_subjects = 0
        for marks in marks_dict.values():
            if marks:
                total_marks += marks.marks_obtained
                total_subjects += 1
        if total_subjects > 0:
            student.total_marks = total_marks
            student.average_marks = total_marks / total_subjects
        else:
            student.total_marks = 0
            student.average_marks = 0
    return render(request, 'teacher/marks/view_marks.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'student_marks': student_marks,
        'mark_types' :mark_types,
        'mark_type' :mark_type,
    })




def edit_all_marks(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student = Student.objects.get(stdnumber=student_id)
        new_marks = {}

        # Get the list of subjects for the class
        schoolclass = student.stdclass
        subjects = Subjects.objects.filter(schoolclasses=schoolclass)

        for subject in subjects:
            subject_id = subject.subjectid
            new_marks[subject_id] = request.POST.get("subject_" + str(subject_id))

            mark = Mark.objects.get(class_name=schoolclass, student_name=student.childname, subject=subject)
            mark.marks_obtained = new_marks[subject_id]
            mark.save()

        messages.success(request, "Marks edited successfully")
        return HttpResponseRedirect("/teacher/his_class/view_marks/{}/{}/".format(schoolclass.classid, teacher.teacherid)) 

    return JsonResponse({})



def edit_teacher_profile(request, teacher_id):
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)
    
    if request.method == 'POST':
        username = request.POST.get("username")
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")
        
        if new_pass == confirm_pass:
            # Update teacher's password (replace this with your actual password update logic)
            teacher.password = new_pass
            teacher.username = username
            teacher.save()
            
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Passwords do not match")
            
        return redirect("Teacher Profile", teacher_id=teacher_id)
    
    return render(request, 'teacher/profile.html', {'teacher': teacher})

    

# generation of a report card

def generate_report(request, student_id):
   # Retrieve student and other data here
    student = Student.objects.get(pk=student_id)
    
    # Construct the URL for the image using STATIC_URL
    image_url = request.build_absolute_uri(settings.STATIC_URL + 'images/rosannalogo.png')

    # Render the report template
    context = {
        "student": student,
        "image_url": image_url,  # Pass the image URL to the template
    }
    html = render_to_string("teacher/reports/report_card.html", context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="report.pdf"'

    # Generate PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    return response


 


