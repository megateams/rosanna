
from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.login, name="Login Page"),
    path('teacher/login/', views.teacher_login, name="Teacher login"),
    path('teacher/logout/', views.logout_view, name='logout'),
    path('teacher/dashboard/', views.dashboard, name="Teacher Dashboard"),
    path('teacher/profile/<teacher_id>', views.profile, name="Teacher Profile"),
    path('teacher/paymenthistory/', views.paymenthistory, name="Payment History"),
]