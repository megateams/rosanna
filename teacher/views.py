from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib import messages
from frontend.models import Teachers, Schoolclasses, Subjects, Student, Mark


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

    # Query the database to get the teacher's information
    try:
        teacher = Teachers.objects.get(teacherid=teacher_id)
    except Teachers.DoesNotExist:
        teacher = None
    return render(request, 'teacher/dashboard.html',{'teacher': teacher})

def profile(request,teacher_id):
    teachers = Teachers.objects.get(teacherid = teacher_id)
    return render(request, 'teacher/profile.html', {'teacher': teachers})    

def paymenthistory(request):
<<<<<<< HEAD
    return render(request, 'teacher/paymenthistory.html')   
=======
    return render(request, 'teacher/paymenthistory.html')  


# marks logic
def addmarks(request):
    # frontend/views.py
    if request.method == 'POST':
        std_id = request.POST['student_name']
        class_id = request.POST['class_name']
        subject_id = request.POST['subject']
        score = request.POST['score']

        # std_obj = Student.objects.get(pk=std_id)
        class_obj = Schoolclasses.objects.get(pk=class_id)
        subject_obj = Subjects.objects.get(pk=subject_id)

        Mark.objects.create(
            class_name=class_obj,
            student_name=std_id,
            subject=subject_obj,
            marks_obtained=score
        )
        Mark.save
        messages.success(request, 'Data successfully added!')
        return redirect('Add Marks')  # Redirect to the same form page after successful form submission
    else:
        selected_students =Student.objects.all()
        # messages.success(request, 'Data not added!')
        return render(request,'teacher/marks/addMarks.html',{'classes': Schoolclasses.objects.all() ,'students': selected_students})

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
def class_details(request, class_id, teacher_id):
    # Retrieve the class and teacher objects based on the provided IDs
    schoolclass = get_object_or_404(Schoolclasses, classid=class_id)
    teacher = get_object_or_404(Teachers, teacherid=teacher_id)

    # Get the students for this class taught by the teacher
    students = Student.objects.filter(stdclass=schoolclass)

    # Get the subjects taught by the teacher for this class
    subjects = teacher.subjects.filter(schoolclasses=schoolclass)

    # Create a dictionary to hold the marks for each student and subject combination
    student_marks = {}
    for student in students:
        marks = Mark.objects.filter(class_name=schoolclass, student_name=student.childname)
        student_marks[student] = {subject: marks.filter(subject=subject).first() for subject in subjects}

    return render(request, 'teacher/class_details.html', {
        'schoolclass': schoolclass,
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
        'student_marks': student_marks,
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

            # Create a new Mark object to save the marks
            Mark.objects.create(
                class_name=schoolclass,
                student_name=student.childname,
                subject=subject,
                marks_obtained=int(marks_obtained),
                mark_type=mark_type,
            )

            # Add a success message to inform the user that marks have been added
            messages.success(request, 'Subject marks added successfully.')
            return redirect('Add Subject marks', class_id=class_id, teacher_id=teacher_id, subject_id=subject_id)

    # If the request method is GET, render the form for adding subject marks
    return render(request, 'teacher/marks/add_subject_marks.html', {
        'schoolclass': schoolclass,
        'subject': subject,
        'students': students.exclude(childname__in=marks_students),
        'mark_types': mark_types,
        'teacher_id': teacher_id,  # Include the teacher_id in the context
    })





>>>>>>> 58beb7021a7a25e052e203b814a2694329acad16

