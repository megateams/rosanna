
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),
    path('studentslist/', views.studentsList, name="Students List"),
    path('addstudent/', views.studentsAdd, name="Add Students"),

    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),

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
    path('add-support-staff/', views.supportstaffAdd, name="Add Support staff "),
    path('show-support-staff/', views.showSupportstaff, name=" Support staff Details"),



    path('staff/', views.staff, name="Staff"),
]