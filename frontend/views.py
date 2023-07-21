from django.shortcuts import render
from django.http import HttpResponse
from .models import Students , Subjects , Schoolclasses , Teachers , Marks

# Create your views here.
def home(request):
    return render(request,'frontend/dashboard.html')

def login(request):
    return render(request, 'frontend/login.html')

def students(request):
    return render(request, 'frontend/students.html')

# def marksform(request):
#     return render(request , 'test/marks.html')

def studentsAdd(request):
    return render(request, 'frontend/student/studentsAdd.html')

# teachers views
def teacherAdd(request):
    return render(request,'frontend/staff/teacherAdd.html')

def teacherList(request):
    return render(request,'frontend/staff/teacherList.html')
# teachers views
# def marks(request):
#     if request.method == 'POST':
#         term = request.POST.get('term')
#         year = request.POST.get('year')
#         studentclass = request.POST.get('studentclass')
#         math = request.POST.get('math')
#         eng = request.POST.get('eng')
#         sci = request.POST.get('sci')
#         sst = request.POST.get('sst')
#         re = request.POST.get('re')
#         computer = request.POST.get('computer')
        
#         Marks.objects.create(
#             term = term ,
#             year = year ,
#             studentclass = studentclass ,
#             math = math ,
#             eng = eng ,
#             sci = sci ,
#             sst = sst , 
#             re = re ,
#             computer = computer
#         )
        
#         Marks.save
#     return HttpResponse('marks submitted')
def student(request):
    if(request.method == 'POST'):
        # stdnumber = request.POST.get('stdnumber')
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

        Students.objects.create(
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
        
        Students.save 
        
    return HttpResponse('Registration Successfull')

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
    
def schoolclasses(request):
    if request.method == 'POST':
        classname = request.POST.get('classname')
        classid = request.POST.get('classid')
        classteacher = request.POST.get('classteacher')
        numofstds = request.POST.get('numofstds')
    
        Schoolclasses.objects.create(
            classname = classname ,
            classid = classid ,
            classteacher = classteacher ,
            numofstds = numofstds 
        )
    
        Schoolclasses.save
    return HttpResponse('Class Created')
    
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
        
        # Teachers.save
    
    return HttpResponse('Teacher created successfully')
    
    
    




