from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib import messages
from frontend.models import *
from finance.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
import os
# from xhtml2pdf import pisa
from django.conf import settings
from django.db.models import Avg
from frontend.views import encryptpassword
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
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

        if teacher and teacher.password == str(encryptpassword(password)):
            # If the credentials are valid, redirect to the teacher dashboard
            request.session['teacher_id'] = teacher.teacherid  # Save the teacher's ID in the session
            return redirect('Teacher Dashboard')  # Replace 'dashboard' with the name/url of your teacher dashboard view

        else:
            # If the credentials are invalid, display an error message
            messages.error(request, 'Invalid username/email or password.')
            return redirect('teacherloginpage')
    

def logout_view(request):
    # Clear session data
    request.session.clear()
    # Add a success message to inform the user about the successful logout
    messages.success(request, 'You have been logged out.')
    # Redirect to the login page
    return redirect('teacherloginpage')

def dashboard(request):
    # Check if the teacher is authenticated (if you are using sessions)
    if 'teacher_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('teacherloginpage')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    teacher_id = request.session['teacher_id']

    teacher = Teachers.objects.get(teacherid=teacher_id)    
    term_data = Term.objects.get(status=1)
    return render(request, 'teacher/dashboard.html',{'teacher': teacher, 'term_data':term_data})

def profile(request,teacher_id):
    teachers = Teachers.objects.get(teacherid = teacher_id)
    return render(request, 'teacher/profile.html', {'teacher': teachers})    


def paymenthistory(request,teacher_id):
    terms = Term.objects.all()

    teacher_payments_data = []
    for term in terms:
        # Get the enrollment data for the current term and year
        term_teacher_payments = Teacherspayment.objects.filter(term=term.current_term, year=term.current_year, teacherid=teacher_id)

        # Create a dictionary for each term's enrollment data
        term_data = {
            'term': term.current_term,
            'year': term.current_year,
            'trpayments_data': term_teacher_payments,
        }

        # Append the term data to the list
        teacher_payments_data.append(term_data)

        print(teacher_payments_data)

    teachers = Teachers.objects.get(teacherid = teacher_id)
    # teacher_data = Teacherspayment.objects.filter(teacherid=teacher_id)

    context ={
        "teacher_payments_data": teacher_payments_data, 'teacher':teachers
        }
    return render(request, 'teacher/paymenthistory.html',context)   

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

from django.core.exceptions import ObjectDoesNotExist

def class_details(request, class_id, teacher_id):
    try:
        # Retrieve the class and teacher objects based on the provided IDs
        schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
        teacher = get_object_or_404(Teachers, teacherid=teacher_id)
        teacher_subject = TeacherSubject.objects.get(schoolclass_id=class_id, teacher_id=teacher_id)

        # Get the students for this class taught by the teacher
        students = Student.objects.filter(stdclass=schoolclass)

        # Get the subjects taught by the teacher for this class
        subjects = teacher_subject.subjects.filter(schoolclasses=schoolclass)

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
            'term_data': Term.objects.get(status=1)
        })

    except ObjectDoesNotExist:
        # Handle the case where TeacherSubject does not exist
        messages.success(request, "You cannot access this class before you are assigned to a subject. Please contact the classteacher")
        return redirect("Teacher Dashboard")



# views.py
def class_marks_by_marktype(request, class_id, teacher_id):
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    teacher = Teachers.objects.get(teacherid=teacher_id)
    mark_type = request.GET.get('marktype')  # Get the mark type from the query parameter
    teacher_subject = TeacherSubject.objects.get(schoolclass_id=class_id, teacher_id=teacher_id)

    students = Student.objects.filter(stdclass=schoolclass)
    subjects = teacher_subject.subjects.filter(schoolclasses=schoolclass)
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

def submit_subject_marks(request, class_id, teacher_id, subject_id):
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
        stdnumber = request.POST.get('studentname')
        marks_obtained = request.POST.get('mark_obtained')

        if mark_type and stdnumber and marks_obtained:
            # Get the student object
            student = Student.objects.get(stdnumber=stdnumber)

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

            return HttpResponseRedirect("/teacher/class_details/addmarks/{}/{}/{}?marktype={}".format(class_id, teacher_id,subject_id,mark_type))  


def addsubjectmarks(request, class_id, teacher_id, subject_id):
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    teacher = Teachers.objects.get(teacherid=teacher_id)
    mark_type = request.GET.get('marktype')

    term_data = Term.objects.all().first()
    students = Student.objects.filter(stdclass=schoolclass)
    subject = Subjects.objects.get(subjectid=subject_id)
    mark_types = Mark.MARK_TYPES
    student_marks = {}
    for student in students:
        marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, mark_type=mark_type)
        student_marks[student] = {subject: marks.filter(subject=subject).first()}
    # Calculate total marks and average marks for each student

    for student, marks_dict in student_marks.items():
        total_marks = 0
        total_subjects = 0
        for marks in marks_dict.values():
            if marks:
                total_marks += marks.marks_obtained
             
        student.total_marks = total_marks
    return render(request, 'teacher/marks/add_subject_marks.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subject': subject,
        'student_marks': student_marks,
        'mark_types' :mark_types,
        'mark_type' :mark_type,
        'term_data': term_data,
    })

def submit_marks(request,class_id,teacher_id):
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)

    # Retrieve the students related to the class
    students = Student.objects.filter(stdclass=schoolclass)

    # Retrieve the subjects that are associated with this class
    subjects = schoolclass.subjects.all()

    # getting the current term data
    term_data = Term.objects.all().first()
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

        return HttpResponseRedirect("/teacher/his_class/addmarks/{}/{}?marktype={}".format(class_id, teacher_id,mark_type))  


def addmarks(request, class_id, teacher_id):
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    teacher = Teachers.objects.get(teacherid=teacher_id)
    mark_type = request.GET.get('marktype')  # Get the mark type from the query parameter
    term_data = Term.objects.all().first()
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
    return render(request, 'teacher/marks/addMarks.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'student_marks': student_marks,
        'mark_types' :mark_types,
        'mark_type' :mark_type,
        'teacher_id' : teacher_id,
        'term_data': term_data
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

def his_class(request, class_id, teacher_id):
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)

    # Get the students for this class taught by the teacher
    students = Student.objects.filter(stdclass=schoolclass)

    mark_types = Mark.MARK_TYPES
    # Get the teachers who teach that class
    teachers_in_class = Teachers.objects.filter(classes=schoolclass)

    # Calculate the number of boys and girls in the class
    num_boys = students.filter(gender='m').count()
    num_girls = students.filter(gender='f').count()

    # Create a dictionary to hold the marks for each student and subject combination
    # student_marks = {}
    # for student in students:
    #     marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname)
    #     student_marks[student] = {subject: marks.filter(subject=subject).first() for subject in subjects}
    
    term_data = Term.objects.get(status=1)

    # Create a dictionary to hold subjects for each teacher_in_class
    teacher_subjects = {}
    for teacher_in_class in teachers_in_class:
        teacher_subject = TeacherSubject.objects.filter(teacher=teacher_in_class, schoolclass=schoolclass).first()
        teacher_subjects[teacher_in_class] = teacher_subject.subjects.all() if teacher_subject else []

    return render(request, 'teacher/his_class.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        # 'student_marks': student_marks,
        'teachers_in_class': teachers_in_class,
        'num_girls': num_girls,
        'num_boys': num_boys,
        'term_data': term_data,
        'mark_types': mark_types,
        'teacher_subjects': teacher_subjects,  # Pass subjects for each teacher_in_class
    })

# view marks
from django.core.exceptions import ObjectDoesNotExist

def assign_subject(request):
    if request.method == "POST":
        teacher_id = request.POST.get("teacher_id")
        schoolclass_id = request.POST.get("schoolclass")
        subjects = request.POST.getlist('subjects')

        # Get the teacher and school class
        teacher = Teachers.objects.get(teacherid=teacher_id)
        schoolclass = Schoolclasses.objects.get(classid=schoolclass_id)

        # Check if the subjects are already assigned to another teacher in the same class
        existing_assignments = TeacherSubject.objects.filter(
            schoolclass=schoolclass, subjects__in=subjects
        ).exclude(teacher=teacher)

        if existing_assignments.exists():
            messages.error(
                request,
                "One or more subjects are already assigned to another teacher in this class."
            )
            return redirect("his_class", class_id=schoolclass_id, teacher_id=teacher_id)

        try:
            # Try to get an existing TeacherSubject record
            data_exists = TeacherSubject.objects.get(schoolclass_id=schoolclass_id, teacher_id=teacher_id)
            
            # Update subjects if the record exists
            data_exists.subjects.set(subjects)
            messages.success(request, "Subjects have been updated successfully")

        except ObjectDoesNotExist:
            # Create a new TeacherSubject record if it doesn't exist
            data = TeacherSubject.objects.create(
                teacher=teacher,
                schoolclass=schoolclass,
            )
            data.subjects.set(subjects)
            messages.success(request, "Teacher assigned subjects for the first time")

        return redirect("his_class", class_id=schoolclass_id, teacher_id=teacher_id)



def view_marks(request, class_id, teacher_id):
    # Retrieve the class and teacher objects based on the provided IDs
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)

    # Get the students for this class taught by the teacher
    students = Student.objects.filter(stdclass=schoolclass)

    try:
        promotion_marks = Promotion.objects.get(class_id=class_id)
    except ObjectDoesNotExist:
        promotion_marks = None

    # Get all subjects
    subjects = Subjects.objects.filter(schoolclasses=schoolclass)
    subjects_count = Subjects.objects.filter(schoolclasses=schoolclass).count()

    mark_types = Mark.MARK_TYPES
    term_data = Term.objects.get(status=1)
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
            marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, subject=subject,current_term=term_data.current_term, current_year=term_data.current_year).exclude(mark_type='Test')

            for mark in marks:
                total_marks += mark.marks_obtained
                marks_count += 1
                subjects_total_marks[subject] += mark.marks_obtained
                subjects_marks_count[subject] += 1

            average_marks = total_marks / 3 if marks_count > 0 else 0
            total_average_marks += int(average_marks)
            final_average = total_average_marks / subjects_count if subjects_count > 0 else 0
              # Accumulate average marks for the student
            student_subjects_data.append({
                'subject': subject,
                'total_marks': total_marks,
                'average_marks': average_marks,
            })
        subjects_marks_data[student] = student_subjects_data
        student.final_average = final_average
        student.total_average_marks = total_average_marks  # Store total average marks for the student

    # Sort the students based on their total marks in descending order
    students = sorted(students, key=lambda student: student.total_average_marks, reverse=True)

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
        'term_data': term_data,
        'promotion_marks': promotion_marks,
    })



# views.py
def view_marks_by_marktype(request, class_id, teacher_id):
    schoolclass = Schoolclasses.objects.get(classid=class_id)
    teacher = Teachers.objects.get(teacherid=teacher_id)
    mark_type = request.GET.get('marktype')  # Get the mark type from the query parameter
    term_data = Term.objects.get(status=1)
    students = Student.objects.filter(stdclass=schoolclass)
    subjects = Subjects.objects.filter(schoolclasses=schoolclass)
    mark_types = Mark.MARK_TYPES
    student_marks = {}
    for student in students:
        marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname, mark_type=mark_type,current_term=term_data.current_term, current_year=term_data.current_year)
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
        'term_data': term_data
    })


def edit_all_marks(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        mark_type = request.POST.get("mark_type")
        teacherid = request.POST.get("teacherid")
        student = Student.objects.get(stdnumber=student_id)
        new_marks = {}

        # Get the list of subjects for the class
        schoolclass = student.stdclass
        subjects = Subjects.objects.filter(schoolclasses=schoolclass)

        for subject in subjects:
            subject_id = subject.subjectid
            new_marks[subject_id] = request.POST.get("subject_" + str(subject_id))

            mark = Mark.objects.get(class_name=schoolclass, student_name=student.childname, subject=subject,mark_type=mark_type)
            if mark:
                mark.marks_obtained = new_marks[subject_id]
                mark.save()
                messages.success(request, "Marks edited successfully")
                return HttpResponseRedirect("/teacher/his_class/view_mark/{}/{}/?marktype={}".format(schoolclass.classid, teacherid,mark_type)) 
            else:
                messages.success(request, "Some marks are empty")
                return HttpResponseRedirect("/teacher/his_class/view_mark/{}/{}/?marktype={}".format(schoolclass.classid, teacherid,mark_type)) 
        

    return JsonResponse({})


def edit_teacher_profile(request, teacher_id):
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)
    
    if request.method == 'POST':
        username = request.POST.get("username")
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")
        
        if new_pass == confirm_pass:
            # Update teacher's password (replace this with your actual password update logic)
            teacher.password = encryptpassword(new_pass)
            teacher.username = username
            teacher.save()
            
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Passwords do not match")
            
        return redirect("Teacher Profile", teacher_id=teacher_id)
    
    return render(request, 'teacher/profile.html', {'teacher': teacher})


# generation of a report card
from collections import defaultdict

def generate_report(request, student_id,position):
    # Retrieve student and other data here
    student = Student.objects.get(pk=student_id)

    # Get the class of the student
    student_class = student.stdclass

    promotion_mark = Promotion.objects.get(class_id=student_class)


    # Fetch the subjects associated with the student's class
    subjects = Subjects.objects.filter(schoolclasses=student_class)

    student_count = Student.objects.filter(stdclass=student_class).count()

    this_class = Schoolclasses.objects.get(pk=student.stdclass.classid)
    classteacher = this_class.classteacher
    # Get mark types except the first one
    mark_types = Mark.MARK_TYPES[1:]

    # Create a dictionary to store marks for each subject and mark type
    student_marks = defaultdict(lambda: defaultdict(list))
    subject_totals = defaultdict(float)  # Dictionary to store total marks for each subject

    # Fetch marks for each subject and mark type
    for subject in subjects:
        for mark_type, _ in mark_types:
            marks = Mark.objects.filter(
                class_name=student_class,
                student_name=student.childname,
                subject=subject,
                mark_type=mark_type,
            )
            student_marks[subject][mark_type] = marks

            # Calculate the total mark for this subject and mark type
            total_mark = sum([mark.marks_obtained for mark in marks])
            subject_totals[subject] += total_mark  # Accumulate total marks for this subject

    # Calculate the average total marks for each subject
    subject_averages = {subject: int(total / len(mark_types)) for subject, total in subject_totals.items()}

    # Calculate the total of subject averages
    total_averages = sum(subject_averages.values())

    # Calculate the final average
    final_average = int(total_averages) / len(subjects)

    # Render the report template
    context = {
        "student": student,
        "term_data": Term.objects.get(status=1),
        "mark_types": mark_types,
        "subjects": subjects,
        "student_marks": student_marks,  # Pass the marks to the template
        "subject_totals": subject_totals,  # Pass the subject totals to the template
        "subject_averages": subject_averages,  # Pass the subject averages to the template
        "total_averages": total_averages,
        "final_average": final_average,
        "position": position,
        "student_count": student_count,
        "classteacher": classteacher,
        "promotion_mark": int(promotion_mark.promotion_mark)
    }

    return render(request, "teacher/reports/report_card.html", context)


# enroll student
def enroll_student(request, classid,teacher_id):
    teacher = Teachers.objects.get(teacherid=teacher_id) 

    term_data = Term.objects.get(status=1)
    students = Student.objects.filter(stdclass=classid)
    that_class = Schoolclasses.objects.get(pk=classid)

    # Get the list of stdnumbers already enrolled for the current term
    enrolled_students = Enrollment.objects.filter(current_term=term_data.current_term, current_year=term_data.current_year, stdclass=that_class).values_list('stdnumber', flat=True)

    # Filter out students who are not yet enrolled for the current term
    not_enrolled_students = students.exclude(pk__in=enrolled_students)

    if request.method == 'POST':
        stdnumber = request.POST.get("stdnumber")
        current_term = request.POST.get("current_term")
        current_year = request.POST.get("current_year")

        student = Student.objects.get(pk=stdnumber)

        if Enrollment.objects.filter(stdnumber=stdnumber, current_term=current_term, stdclass=that_class).exists():
            messages.success(request, "Student has already been enrolled")
            return redirect("enroll_student", classid=classid, teacher_id=teacher_id)

        else:
            enroll = Enrollment.objects.create(
                stdnumber=student,
                current_term=current_term,
                current_year=current_year,
                stdclass=that_class,
            )

            enroll.save()

            messages.success(request, "Student successfully enrolled")
            return redirect("enroll_student", classid=classid, teacher_id=teacher_id)

    context = {
        'term_data': term_data,
        'students': not_enrolled_students,
        'class': that_class,
        'teacher': teacher,
        'enrolled': enrolled_students,
    }
    return render(request, 'teacher/enroll_student.html', context)


# enrollment history
def enrollment_history(request, classid, teacher_id):
    teacher = Teachers.objects.get(teacherid=teacher_id)
    terms = Term.objects.all()

    that_class = Schoolclasses.objects.get(pk=classid)
    this_term = Term.objects.get(status=1)
    enrollment_data = []

    for term in terms:
        # Get the enrollment data for the current term and year
        enrollment_for_term = Enrollment.objects.filter(current_term=term.current_term, current_year=term.current_year, stdclass_id=classid)

        # Create a dictionary for each term's enrollment data
        term_data = {
            'term_name': term.current_term,
            'term_year': term.current_year,
            'enrollment_data': enrollment_for_term,
        }

        # Append the term data to the list
        enrollment_data.append(term_data)

    context = {
        'enrollment_data': enrollment_data,
        'this_term': this_term,
        'class': that_class,
        'teacher': teacher
    }

    return render(request, 'teacher/enrollment_history.html', context)


# set promotion mark
def set_promotion_mark(request,class_id,teacher_id):
    if request.method == "POST":
        promotion_mark = request.POST.get("promotion_mark")

        that_class = Schoolclasses.objects.get(pk=class_id)
        
        try:
            promotion_list = Promotion.objects.get(class_id=class_id)
        except ObjectDoesNotExist:
            promotion_list = None

        if promotion_list:
            promotion = Promotion.objects.create(promotion_mark=promotion_mark,class_id=that_class)
            promotion.save()
            messages.success(request, "Promotion mark updated successfully")
            return redirect('View Marks',class_id=class_id,teacher_id=teacher_id)

        else:

            promotion = Promotion.objects.create(promotion_mark=promotion_mark,class_id=that_class)
            promotion.save()

            messages.success(request, "Promotion mark set successfully")
            return redirect('View Marks',class_id=class_id,teacher_id=teacher_id)

 


