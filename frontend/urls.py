
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),
    path('studentslist/', views.studentsList, name="Students List"),
    path('addstudent/', views.studentsAdd, name="Add Students"),
    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),
    path('staff/', views.staff, name="Staff"),
]