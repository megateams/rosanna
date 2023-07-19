from django.urls import path
from . import views
# from .views import save_registration

urlpatterns = [
    path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),

    path('students/', views.students, name="Students"),
    # path('save_registration/', save_registration, name='save_registration')
    path('studentslist/', views.studentsList, name="Students List"),
    path('addstudent/', views.studentsAdd, name="Add Students"),

    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),

    path('showstudent/', views.showStudent, name="Student details"),

    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="Add Support staff "),
    path('show-support-staff/', views.showSupportstaff, name=" Support staff Details"),



    path('staff/', views.staff, name="Staff"),
]