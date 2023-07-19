
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),
    path('students/', views.students, name="Students"),

]