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

    path('students/', views.students, name="Students"),
    # path('save_registration/', save_registration, name='save_registration')
    path('studentslist/', views.studentsList, name="Students List"),
    path('addstudent/', views.studentsAdd, name="AddStudents"),
    path('addstudent/submit/', views.studentReg, name="studentReg"),
    # path('addstudent/', views.studentsAdd, name="Add Students"),
    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),
    path('addteacher/submit/', views.teachers, name="Teachers"),

    path('addusers/', views.addUsers, name="Add User"),
    path('userslist/', views.usersList, name="View List"),

    path('addmarks/', views.addMarks, name="Add Marks"),
    path('markslist/', views.marksList, name=" View Marks"),  
    path('get_subjects/<int:class_id>/', views.get_subjects, name='get_subjects'),  

    path('showstudent/', views.showStudent, name="Student details"),
    path('get_students_by_class/<int:class_id>/', views.get_students_by_class, name='get_students_by_class'),


    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="AddSupportstaff"),
    path('showteacher/<teacherId>', views.showteacher, name=" Show Teacher"),
    path('add-support-staff/submit/', views.supportstaffreg, name='supportstaffreg'),
    # path('add-support-staff/', views.supportstaffreg, name='supportstaffreg'),

    path('staff/', views.staff, name="Staff"),
    path('showsubjects/' , views.showsubjects , name='showsubjects'),
    path('addsubjectsform/' , views.addsubjectsform , name = "addsubjectsform"),
    path('addsubject/' , views.addsubject , name = 'addsubject'),
    path('showclasses/' , views.showclasses , name='showclasses'),
    path('addclasses/sendclasses/' , views.schoolclasses , name = 'schoolclasses'),
    path('addclasses/' , views.addclasses , name='AddClasses'),
]