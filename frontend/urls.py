from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import save_registration

urlpatterns = [
    # Login and Logout URLs
    # path("login/", auth_views.LoginView.as_view(template_name="frontend/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    # path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),

    path('addstudent/submit/', views.studentsReg, name="StudentsReg"),
    path('studentslist/', views.studentsList, name="Students List"),
    path('showstudent/<studentId>', views.Showstudents, name="Showstudents"),
    path('addstudent/', views.studentsAdd, name="AddStudents"),
    path('export-excel', views.export_to_excel, name="export_excel"),
    path('deletestudent/<stdnumber>', views.DeleteStudent, name="deleteStudent"),
    

    # path('addstudent/', views.studentsAdd, name="Add Students"),
    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),
    path('teacher_export_excel/', views.teacher_export_to_excel, name="teacher_export_excel"),
    path('deleteteacher/<teacherid>', views.DeleteTeacher, name="delete_teacher"),

    path('addusers/', views.addUsers, name="Add User"),
    path('userslist/', views.usersList, name="View List"),

    path('addclass/', views.addClass, name="Add Class"),
    path('classlist/', views.classList, name=" View Classes"), 

    path('addsubject/', views.addSubject, name="Add Subject"),
    path('subjectlist/', views.subjectList, name=" View Subjects"),

    path('addmarks/', views.addMarks, name="Add Marks"),
    path('markslist/', views.marksList, name=" View Marks"),    

    path('showstudent/', views.showStudent, name="Student details"),

    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="AddSupportstaff"),
    path('show-support-staff/', views.showSupportstaff, name=" Support staff Details"),
    path('add-support-staff/submit/', views.supportstaffreg, name='supportstaffreg'),
    path('support-export-excel/', views.support_staff_export_to_excel, name='support_export_excel'),
    path('deletesupportstaff/<int:id>', views.DeleteSupportStaff, name ="deleteSupportStaff"),
    # path('add-support-staff/', views.supportstaffreg, name='supportstaffreg'),

    path('staff/', views.staff, name="Staff"),
    path('showsubjects/' , views.showsubjects , name='showsubjects'),
    path('showsubjects/addsubjectsform/' , views.addsubjectsform , name = "addsubjectsform"),
    path('addsubject/' , views.addsubject , name = 'addsubject'),
    path('showclasses/' , views.showclasses , name='showclasses'),
    path('sendclasses/' , views.schoolclasses , name = 'schoolclasses'),
    path('showclasses/addclasses/' , views.addclasses , name='showclasses'),
]