from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib import messages
from .models import *
from django.db.models import Sum
from finance.models import Feesstructure, ExpenseRecord
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .decorators import admin_required

# Create your views here.
# creating views for dashboard
def deletemarks(request , id):
    marks = Marks.objects.filter(id = id)
    marks.delete()
    messages.success(request , 'Marks Deleted')
    return redirect('viewmarks')

def DeleteStudent(request , stdnumber):
    student = Student.objects.filter(stdnumber = stdnumber)
    student.delete()
    messages.success(request, 'Student Deleted Successfully')
    return redirect('Studentslist')

def DeleteSupportStaff(request , id):
    supportstaff = Supportstaff.objects.filter(id = id)
    supportstaff.delete()
    messages.success(request, 'Support stuff deleted')
    return redirect('deleteSupportStuff')

def Support_Staff_list_View(request):
    supportstafflist = Supportstaff.objects.all()
    return render(request , 'frontend/staff/supportstaffList.html' , {'supportstafflist':supportstafflist})

def deleteclass(request, classid):
    classes = Schoolclasses.objects.filter(classid = classid)
    classes.delete()
    messages.success(request, 'Class deleted')
    return redirect("showclasses")

def deletesubject(request , subjectid):
    subject = Subjects.objects.filter(subjectid = subjectid)
    subject.delete()
    messages.success(request, 'Subject deleted')
    return redirect("Subjects")
    
def home(request):
    if request.session.get('logged_out', False):
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("login")

    boys_count = Student.objects.filter(gender='m').count()
    girls_count = Student.objects.filter(gender='f').count()

    teacher_count = Teachers.objects.count()
    student_count = Student.objects.count()
    support_staff_count = Supportstaff.objects.count()

    classes = Schoolclasses.objects.all()

    # Calculate the number of boys and girls in each class and store in lists
    boys_count_by_class = []
    girls_count_by_class = []
    class_names = []
    for class_obj in classes:
        b_count = Student.objects.filter(stdclass=class_obj, gender='m').count()
        g_count = Student.objects.filter(stdclass=class_obj, gender='f').count()
        boys_count_by_class.append(b_count)
        girls_count_by_class.append(g_count)
        class_names.append(class_obj.classname)
        
    context = {
        'boys_count' : boys_count,
        'girls_count': girls_count,
        'teacher_count': teacher_count,
        'student_count': student_count,
        'support_staff_count': support_staff_count,

        'boys_count_by_class': boys_count_by_class,
        'girls_count_by_class': girls_count_by_class,
        'class_names': class_names,
    }
    return render(request,'frontend/dashboard.html',context)

#register details for the user (admin)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, "frontend/registration.html", {"form": form})

# login views for the admin user
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            request.session.pop('logged_out', None) # clear logout session variable in login
            return redirect("Dashboard")
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, "frontend/login.html")

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    request.session['logged_out'] = True # Set the session variable to True
    return redirect("login") # Redirect to the login page after logout

# def login(request):
    #retrieve the login crudentials from the database
    # login_details =Login.objects.all()
    # return render(request, 'frontend/login.html')

def students(request):
    return render(request, 'frontend/students.html')

# students views
def studentsList(request):
    #retrieve all the selected students data from the database
    selected_students =Student.objects.values('stdnumber', 'childname','stdclass', 'gender', 'dob', 'address', 'house', 'regdate', 'fathername', 'mothername')
    # all_students_list =Student.objects.all()
    #pass the data to template for rendering
    return render(request, 'frontend/student/studentsList.html', {'students': selected_students})

def studentsAdd(request):
    return render(request, 'frontend/student/studentsAdd.html',{'classes': Schoolclasses.objects.all()})


# teachers views
def teacherAdd(request):
    classes = Schoolclasses.objects.all()
    subjects = Subjects.objects.all()
    return render(request,'frontend/staff/teacherAdd.html', {'classes': classes, 'subjects':subjects})

def teacherList(request):
    teachers = Teachers.objects.all()
    return render(request,'frontend/staff/teacherList.html', {'teachers': teachers})
# teachers views

# users views
def addUsers(request):
    return render(request,'frontend/users/addUsers.html')

def usersList(request):
    return render(request,'frontend/users/usersList.html')
# users views

def get_subjects(request, class_id):
    class_obj = get_object_or_404(Schoolclasses, pk=class_id)
    subjects = class_obj.subjects.all().values('subjectid', 'subjectname')
    return JsonResponse(list(subjects), safe=False)

# classes views
# def addClass(request):
#     return render(request,'frontend/classes/addClass.html')

# def classList(request):
#     return render(request,'frontend/classes/classList.html')
# classes views

# marks views

def addmarks(request):
    studentdata = Student.objects.all()
    studentnumber = Student.objects.filter(stdnumber)
    return render(request,'frontend/marks/addMarks.html', {'students': studentdata})

def submitmarks(request):
    # studentnumbers = Marks.objects.values_list('stdnum_id')
    #render(request, 'frontend/marks/addmarks.html' , {'stdnumbers':studentnumbers})
    if request.method == 'POST':
        stdnum = request.POST.get('stdnum')
        term = request.POST.get('term')
        year = request.POST.get('year')
        studentclass = request.POST.get('studentclass')
        math = request.POST.get('math')
        eng = request.POST.get('eng')
        sci = request.POST.get('sci')
        sst = request.POST.get('sst')
        re = request.POST.get('re')
        computer = request.POST.get('computer')
        
        Marks.objects.create(
            stdnum = stdnum ,
            term = term ,
            year = year ,
            studentclass = studentclass ,
            math = math ,
            eng = eng ,
            sci = sci ,
            sst = sst ,
            re = re ,
            computer = computer 
        )
        
        Marks.save
    marks = Marks.objects.all()
    return render(request,'frontend/marks/marksList.html' , {'marks':marks})

def marksList(request):
    marks = Marks.objects.all()
    return render(request,'frontend/marks/marksList.html' , {'marks':marks})
# marks views


# subjects views
def addSubject(request):
    if request.method == 'POST':
        subjectname = request.POST.get('subjectname')
        subjectid = request.POST.get('subjectid')
        level = request.POST.get('classlevel')
        subjecthead = request.POST.get('subjecthead')
        
        Subjects.objects.create(
            subjectname = subjectname ,
            subjectid = subjectid ,
            classlevel = level ,
            subjecthead = subjecthead ,
        )
        
        Subjects.save
    return render(request,'frontend/subjects/addSubject.html')

def subjectList(request):
    subjects = Subjects.objects.all
    return render(request,'frontend/subjects/subjectList.html',{'subjects':subjects})
# classes views

def showStudent(request):
    return render(request, 'frontend/student/showStudent.html')
def addMarks(request):
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
        return render(request,'frontend/marks/addMarks.html',{'classes': Schoolclasses.objects.all() ,'students': selected_students})

def marksList(request):
    return render(request,'frontend/marks/marksList.html', {'marks': Mark.objects.all()})
# marks views

def showStudent(request,stdnumber):
    student = Student.objects.get(stdnumber = stdnumber)
    return render(request, 'frontend/student/showStudent.html', {'student': student})
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
        messages.success(request, 'Data successfully added!')
                
        # Redirect to the registration page for support staff after successful data addition
        return redirect('AddSupportstaff')
    
def showsubjects(request):
    subjects = Subjects.objects.all()
    return render(request , 'frontend/academics/subjects.html' , {'subjects' : subjects})

def addsubjectsform(request):
    return render(request, 'frontend/academics/addsubjects.html')

def addsubject(request):
    if request.method == 'POST':
        subjectname = request.POST.get('subjectname')
        subjectid = request.POST.get('subjectid')
        classlevel = request.POST.get('classlevel')
        subjecthead = request.POST.get('subjecthead')
        
        Subjects.objects.create(
            subjectname = subjectname ,
            subjectid = subjectid ,
            classlevel = classlevel ,
            subjecthead = subjecthead ,
        )
        
        Subjects.save
        messages.success(request, 'Subject successfully added!')
        return redirect("addsubjectsform")
    # return render(request , 'frontend/academics/subjects.html' , {'subjects' : Subjects.objects.all()})

def supportstaffList(request):
    # Retrieve all support staff data from the database
    all_support_staff = Supportstaff.objects.all()
    # Pass the data to the template for rendering
    return render(request, 'frontend/staff/supportstaffList.html', {'support_staff': all_support_staff})
    
def showteacher(request,teacherId):
    teachers = Teachers.objects.filter(teacherid=teacherId)
    return render(request, 'frontend/staff/showteacher.html',{'teachers': teachers})
# support staff views

def staff(request):
    return render(request, 'frontend/staff.html')



#students registration views
def studentReg(request):
    if(request.method == 'POST'):
        stdnumber = request.POST.get('stdnumber')
        regdate = request.POST.get('regdate')
        childname = request.POST.get('childname')
        # stdclass = request.POST.get('stdclass')
        class_id = request.POST['stdclass']
        selected_class = Schoolclasses.objects.get(pk=class_id)
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        house = request.POST.get('house')
        # studentclass = request.POST.get('studentclass')
        fathername = request.POST.get('fathername')
        fcontact = request.POST.get('fcontact')
        foccupation = request.POST.get('foccupation')
        mothername = request.POST.get('mothername')
        mcontact = request.POST.get('mcontact')
        moccupation = request.POST.get('moccupation')
        livingwith = request.POST.get('livingwith')
        guardianname = request.POST.get('guardianname')
        gcontact = request.POST.get('gcontact')
        student =Student.objects.create(
            stdnumber =stdnumber,            
            regdate = regdate ,
            childname = childname ,
            stdclass=selected_class,
            gender = gender ,
            dob = dob ,
            address = address ,
            house = house ,
            # studentclass = studentclass , 
            fathername = fathername ,
            fcontact = fcontact ,
            foccupation = foccupation ,
            mothername = mothername , 
            mcontact = mcontact ,
            moccupation = moccupation ,
            livingwith = livingwith ,
            guardianname = guardianname ,
            gcontact = gcontact
        )        
        student.save ()
        messages.success(request, 'Data successfully added!')
        return redirect("AddStudents")
        # return HttpResponse('Registration Successful')

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

def subjects(request):
    if request.method == 'POST':
        subjectnames = request.POST.get('subjectname')
        subjectids = request.POST.get('subjectid')
        classlevel = request.POST.get('classlevel')
        subjectheads = request.POST.get('subjecthead')
    
        Subjects.objects.create(
            subjectname = subjectnames , 
            subjectid = subjectids , 
            classlevel = classlevel , 
            subjecthead = subjectheads
        )
    
        Subjects.save
    return HttpResponse(subjectnames)

from django.shortcuts import render
from .models import Schoolclasses, Teachers

def showclasses(request):
    classes = Schoolclasses.objects.all()
    return render(request , 'frontend/classes/classList.html' , {'classes':classes})
    # Retrieve the teacher names based on teacherid matching classname
    teachers = Teachers.objects.all()
    return render(request, 'frontend/academics/showclasses.html', {'classes': classes, 'teachers': teachers})
    return render(request , 'frontend/classes/classList.html' , {'classes':classes})

def addclasses(request):
    return render(request , 'frontend/academics/addclasses.html')
    # classes = Schoolclasses.objects.all()
    # return render(request , 'frontend/academics/addclasses.html' , {'classes':classes})
    
def schoolclasses(request):
    if request.method == 'POST':
        classname = request.POST.get('classname')
        classid = request.POST.get('classid')
        classteacher = request.POST.get('classteacher')
        classlevels = request.POST.get('classlevel')
        numofstds = request.POST.get('numofstds')
    
        Schoolclasses.objects.create(
            classname = classname ,
            classid = classid ,
            classlevels = classlevels ,
            classteacher = classteacher ,
            numofstds = numofstds 
        )
    
        Schoolclasses.save
        classes = Schoolclasses.objects.all()
    return render(request , 'frontend/classes/classList.html' , {'classes':classes})
    
def teachers(request):
    if request.method == 'POST':
        teacherid = request.POST.get('teacherid')
        teachernames = request.POST.get('teachernames')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        classes = request.POST.get('classes')
        joiningdate = request.POST.get('joiningdate')
        position = request.POST.get('position')
        subject = request.POST.get('subject')
        qualification = request.POST.get('qualification')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        Teachers.objects.create(
            teacherid = teacherid ,
            teachernames = teachernames ,
            dob = dob ,
            gender = gender ,
            contact = contact ,
            email = email ,
            address = address ,
            classes = classes ,
            joiningdate = joiningdate ,
            position = position ,
            subject = subject , 
            qualification = qualification ,
            username = username , 
            password = password
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
    subjects = Subjects.objects.all()
    teachers = Teachers.objects.all()
    return render(request , 'frontend/academics/addclasses.html' , {'subjects':subjects, 'teachers':teachers})
    
def schoolclasses(request):
    if request.method == 'POST':
        classname = request.POST['class_name']
        subject_names = request.POST.getlist('subjects')
        classteacher = request.POST['classteacher']
        class_level = request.POST['class_level']

        newclass = Schoolclasses.objects.create(classname=classname,classteacher=classteacher,class_level=class_level)

        for subject_name in subject_names:
            subject, created = Subjects.objects.get_or_create(subjectname=subject_name)
            newclass.subjects.add(subject)

        messages.success(request, 'Class successfully added!')
        return redirect("AddClasses")
    # return render(request , 'frontend/academics/showclasses.html',{'classes' : Schoolclasses.objects.all()})   

#Export the data in excel in the students model
def export_to_excel(request):
    #fetch all the data from the database
        data =Student.objects.all().values_list(
            'stdnumber', 'childname', 'gender', 'dob', 'address', 'house', 'studentclass', 'regdate', 'fathername','fcontact','foccupation', 'mothername', 'mcontact', 'moccupation', 'livingwith', 'guardianname','gcontact'
            )
        
        #create new workbook and add in a worksheet
        wb =openpyxl.Workbook()
        ws =wb.active
        
        #write field names to the worksheet as headers
        # field_names = Student._meta.get_fields()
        # header_row = [field.name for field in field_names]
        # ws.append(header_row)
        
        #write data to the worksheet
        ws.append(['Student Number', 'Student Name', 'Gender', 'DOB', 'Address', 'House', 'Class', 'Reg Date', "Father's name",'Father\'s Contact','Foccupation', 'Mother\'s Name', 'Mother\'s contact', 'Moccupation', 'Livingwith', 'Guardian\'s Name','gcontact'])
        for row_data in data:
            ws.append(row_data)
            
        # Set the filename and content type for the response
        filename = 'exported_data.xlsx'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        #save the workboot to the response
        wb.save(response)
        
        return response
#Export the data in excel in the support staff model
def support_staff_export_to_excel(request):
    #fetch all the data from the database
        data =Supportstaff.objects.all().values()
        #create new workbook and add in a worksheet
        wb =openpyxl.Workbook()
        ws =wb.active
        
        #write field names to the worksheet as headers
        field_names = Supportstaff._meta.get_fields()
        header_row = [field.name for field in field_names]
        ws.append(header_row)
        
        #write data to the worksheet
        for row_data in data:
            ws.append(list(row_data.values()))
            
        # Set the filename and content type for the response
        filename = 'exported_data.xlsx'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        #save the workboot to the response
        wb.save(response)
        
        return response


#Export the data in excel in the Teacher's model
def teacher_export_to_excel(request):
    #fetch all the data from the database
        data =Teachers.objects.all().values_list(
            'teacherid', 'teachernames', 'dob', 'gender', 'contact', 'email', 'address', 'classes', 'joiningdate','position','subject', 'qualification'
            )
        
        #create new workbook and add in a worksheet
        wb =openpyxl.Workbook()
        ws =wb.active
        
        #write field names to the worksheet as headers
        # field_names = Student._meta.get_fields()
        # header_row = [field.name for field in field_names]
        # ws.append(header_row)
        
        #write data to the worksheet
        ws.append(['Teacher ID', 'Name', 'DOB', 'Gender', 'Contact', 'Email', 'Address', 'Classes Taught', 'Date Joined','Position','Subject', 'Qualification'])
        for row_data in data:
            ws.append(row_data)
            
        # Set the filename and content type for the response
        filename = 'teacher\'s_data.xlsx'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        #save the workboot to the response
        wb.save(response)
        
        return response
        
    # return render(request , 'frontend/academics/showclasses.html',{'classes' : Schoolclasses.objects.all()})
    
def teachers(request):
    if request.method == 'POST':
        
        last_teacher = Teachers.objects.order_by('-teacherid').first()

        # Generate default ID and password
        default_teacherid = 'RT{:04}'.format(int(last_teacher.teacherid[2:]) + 1) if last_teacher else 'RT0001'
        default_password = "123456"

        # teacherid = request.POST.get('teacherid')
        teachernames = request.POST.get('teachernames')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        joiningdate = request.POST.get('joiningdate')
        classes = request.POST.getlist('classes')  # Get a list of selected classes
        subjects = request.POST.getlist('subjects')  # Get a list of selected subjects
        position = request.POST.get('position')
        qualification = request.POST.get('qualification')
        username = request.POST.get('username')
        # password = request.POST.get('password')


        # Create and save the Teacher object to the database
        teacher = Teachers.objects.create(
            teacherid=default_teacherid,
            teachernames=teachernames,
            gender=gender,
            dob=dob,
            contact=contact,
            email=email,
            address=address,
            joiningdate=joiningdate,
            position=position,
            qualification=qualification,
            username=username,
            password=default_password
        )
        teacher.save()

        # Add the selected classes and subjects to the teacher object
        teacher.classes.set(classes)
        teacher.subjects.set(subjects)

        # Display a success message to the user
        messages.success(request, 'Teacher added successfully!')

        # Redirect the user to a different page (e.g., teacherlist page)
        return redirect('Add Teacher')
   
def supportstaffList(request):
    # Retrieve all support staff data from the database
    all_support_staff = Supportstaff.objects.all()
    # Pass the data to the template for rendering
    return render(request, 'frontend/staff/supportstaffList.html', {'support_staff': all_support_staff})
# Accounting
def feesstructure(request):
    feesstructure = Feesstructure.objects.all()
    return render(request, 'frontend/accounting/feesstructure.html',{"feesstructure": feesstructure})

def fees(request):
    return render(request, 'frontend/accounting/fees.html')
    
def teacherspayments(request):
    return render(request, 'frontend/accounting/teacherspayments.html')
def supportstaffpayments(request):
    return render(request, 'frontend/accounting/supportstaffpayments.html')

def expenses(request):
    total_amount_paid = ExpenseRecord.objects.aggregate(Sum('amountpaid'))['amountpaid__sum']
    expenses = ExpenseRecord.objects.all()
    context = {
        'expenses': expenses,
        'total_amount_paid': total_amount_paid,
        }
    return render(request, 'frontend/accounting/expenses.html',context)

def expenses(request):
    return render(request, 'frontend/accounting/expenses.html')

