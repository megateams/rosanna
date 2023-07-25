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
    

    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),

    path('showstudent/', views.showStudent, name="Student details"),

    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="AddSupportstaff"),
    path('show-support-staff/', views.showSupportstaff, name=" Support staff Details"),
    #submit the template data url
    path('add-support-staff/submit/', views.supportstaffreg, name='supportstaffreg'),
    # path('add-support-staff/', views.supportstaffreg, name='supportstaffreg'),

    path('staff/', views.staff, name="Staff"),

]