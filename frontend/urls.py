
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),
    path('studentslist/', views.studentsList, name="Students List"),
    path('addstudent/', views.studentsAdd, name="Add Students"),
    path('showstudent/', views.showStudent, name="Student details"),

    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="Add Support staff "),
    path('show-support-staff/', views.showSupportstaff, name=" Support staff Details"),


    path('staff/', views.staff, name="Staff"),
]