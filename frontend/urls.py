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
    path('add-support-staff/', views.supportstaffAdd, name="AddSupportstaff"),
    path('show-support-staff/', views.showSupportstaff, name=" Support staff Details"),
    #test
    path('add-support-staff/submit/', views.supportstaffreg, name='supportstaffreg'),
    # path('add-support-staff/', views.supportstaffreg, name='supportstaffreg'),

    path('staff/', views.staff, name="Staff"),
    path('showsubjects/' , views.showsubjects , name='showsubjects'),
    path('showsubjects/addsubjectsform/' , views.addsubjectsform , name = "addsubjectsform"),
    path('addsubject' , views.addsubject , name = 'addsubject'),
    path('showclasses/' , views.showclasses , name='showclasses'),
    path('sendclasses/' , views.schoolclasses , name = 'schoolclasses'),
    path('showclasses/addclasses/' , views.addclasses , name='showclasses'),
]