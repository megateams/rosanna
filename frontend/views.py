from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'frontend/dashboard.html')

def login(request):
    return render(request, 'frontend/login.html')

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

# users views
def addUsers(request):
    return render(request,'frontend/users/addUsers.html')

def usersList(request):
    return render(request,'frontend/users/usersList.html')
# users views

def showStudent(request):
    return render(request, 'frontend/student/showStudent.html')
# students views

# support staff views
def supportstaffAdd(request):
    return render(request, 'frontend/staff/supportstaffAdd.html')

def supportstaffList(request):
    return render(request, 'frontend/staff/supportstaffList.html')

def showSupportstaff(request):
    return render(request, 'frontend/staff/showSupportstaff.html')
# support staff views


def staff(request):
    return render(request, 'frontend/staff.html')
