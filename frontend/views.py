from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import openpyxl

# Create your views here.
# creating views for dashboard
def home(request):
    if request.session.get('logged_out', False):
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("login")
    
    return render(request,'frontend/dashboard.html')
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

# login views for the admin user login
def user_login(request):
    if request.user.is_authenticated:
        return redirect("Dashboard")  # Redirect to the dashboard if the user is already logged in       
    
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
    return render(request, "frontend/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    request.session['logged_out'] = True # Set the session variable to True
    return redirect("login") # Redirect to the login page after logout


#students registration views
def studentsReg(request):
    if(request.method == 'POST'):
        stdnumber = request.POST.get('stdnumber')
        # Check if the student with the given stdnumber already exists in the database
        if Student.objects.filter(stdnumber=stdnumber).exists():
            messages.error(request, f"Student with student number {stdnumber} already exists.")
            return redirect("AddStudents")
        regdate = request.POST.get('regdate')
        childname = request.POST.get('childname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        house = request.POST.get('house')
        studentclass = request.POST.get('studentclass')
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
            gender = gender ,
            dob = dob ,
            address = address ,
            house = house ,
            studentclass = studentclass , 
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
    
# students views
def studentsList(request):
    #retrieve all the selected students data from the database
    selected_students =Student.objects.values('stdnumber', 'childname', 'gender', 'dob', 'address', 'house', 'regdate', 'fathername', 'mothername')
    # all_students_list =Student.objects.all()
    #pass the data to template for rendering
    return render(request, 'frontend/student/studentsList.html', {'students': selected_students})
def Showstudents(request,studentId):
    #retrieve all the selected students data from the database
    selected_show_students = Student.objects.filter(stdnumber=studentId)
    #pass the data to template for rendering
    return render(request, 'frontend/student/showStudent.html', {'showstudents': selected_show_students})

def studentsAdd(request):
    return render(request, 'frontend/student/studentsAdd.html')

#Delete student views
def DeleteStudent(request, stdnumber):
    delete_student =Student.objects.filter(stdnumber =stdnumber)
    delete_student.delete()
    messages.success(request, "The data deleted successfully")
    return redirect("Students List")

# teachers views
def teacherAdd(request):
    return render(request,'frontend/staff/teacherAdd.html')

#Teachers views   
def teachers(request):
    if request.method == 'POST':
        teacherid = request.POST.get('teacherid')
        if Teachers.objects.filter(teacherid=teacherid).exists():
            messages.error(request, f"Teacher with ID {teacherid} already exists.")
            return redirect("Add Teacher")
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
        
        teacher =Teachers.objects.create(
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
        teacher.save()
        messages.success(request, "Teacher has been successfully added!")
        return redirect("Add Teacher") 
    
def teacherList(request):
    select_teachers = Teachers.objects.all()
    return render(request,'frontend/staff/teacherList.html', {'teachers': select_teachers})
# teachers views
def showteacher(request,teacherId):
    teachers = Teachers.objects.filter(teacherid=teacherId)
    return render(request, 'frontend/staff/showteacher.html',{'teachers': teachers})

#Delete Teacher views
def DeleteTeacher(request, teacherid):
    delete_teacher =Teachers.objects.filter(teacherid =teacherid)
    delete_teacher.delete()
    messages.success(request, "The data deleted successfully")
    return redirect("Teachers List")

# users views
def addUsers(request):
    return render(request,'frontend/users/addUsers.html')

def usersList(request):
    return render(request,'frontend/users/usersList.html')
# users views


# marks views
def addMarks(request):
    return render(request,'frontend/marks/addMarks.html')

def marksList(request):
    return render(request,'frontend/marks/marksList.html')
# marks views

# fees views
def addFees(request):
    return render(request,'frontend/fees/addFees.html')

def feesList(request):
    return render(request,'frontend/fees/feesList.html')
# fees views

# staffpayments views
def addStaffpayments(request):
    return render(request,'frontend/staffpayments/addStaffpayments.html')

def staffpaymentsList(request):
    return render(request,'frontend/staffpayments/staffpaymentsList.html')
# staffpayments views

# expenses views
def addExpenses(request):
    return render(request,'frontend/expenses/addExpenses.html')

def expensesList(request):
    return render(request,'frontend/expenses/expensesList.html')
# expenses views

def showStudent(request):
    return render(request, 'frontend/student/showStudent.html')
# students views

# support staff views
def supportstaffAdd(request):
      return render(request, 'frontend/staff/supportstaffAdd.html')

# Send the registration support staff details to and retrieve from database 
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

def supportstaffList(request):
    # Retrieve all support staff data from the database
    all_support_staff = Supportstaff.objects.all()
    # Pass the data to the template for rendering
    return render(request, 'frontend/staff/supportstaffList.html', {'support_staff': all_support_staff})
    
def showSupportstaff(request):
    return render(request, 'frontend/staff/showSupportstaff.html')

#delete support staff views
def DeleteSupportStaff(request, id):
    support_staff =Supportstaff.objects.filter(id =id)
    support_staff.delete()
    messages.success(request, "Data deleted successfully")
    return redirect("Support staff List")

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

def staff(request):
    return render(request, 'frontend/staff.html')

#students registration views
# def studentReg(request):

def supportstaffList(request):
    # Retrieve all support staff data from the database
    all_support_staff = Supportstaff.objects.all()
    # Pass the data to the template for rendering
    return render(request, 'frontend/staff/supportstaffList.html', {'support_staff': all_support_staff})
    
def staff(request):
    return render(request, 'frontend/staff.html')



#students registration views
def studentReg(request):
    if(request.method == 'POST'):
        stdnumber = request.POST.get('stdnumber')
        regdate = request.POST.get('regdate')
        childname = request.POST.get('childname')
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

def subjects(request):
    if request.method == 'POST':
        subjectnames = request.POST.get('subjectname')
        subjectids = request.POST.get('subjectid')
        classlevels = request.POST.get('classlevel')
        subjectheads = request.POST.get('subjecthead')
    
        Subjects.objects.create(
            subjectname = subjectnames , 
            subjectid = subjectids , 
            classlevel = classlevels , 
            subjecthead = subjectheads
        )
    
        Subjects.save
    return HttpResponse(subjectnames)

def showclasses(request):
    classes = Schoolclasses.objects.all()
    return render(request , 'frontend/academics/showclasses.html' , {'classes':classes})

def addclasses(request):
    classes = Schoolclasses.objects.all()
    return render(request , 'frontend/academics/addclasses.html' , {'classes':classes})
    
def schoolclasses(request):
    if request.method == 'POST':
        classname = request.POST.get('classname')
        classid = request.POST.get('classid')
        classteacher = request.POST.get('classteacher')
        classlevel = request.POST.get('classlevel')
        numofstds = request.POST.get('numofstds')
    
        Schoolclasses.objects.create(
            classname = classname ,
            classid = classid ,
            classlevel = classlevel ,
            classteacher = classteacher ,
            numofstds = numofstds 
        )
    
        Schoolclasses.save
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

        
