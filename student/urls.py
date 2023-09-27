
from django.urls import path,include
from . import views

urlpatterns = [
    path('student/', views.login, name="Login Page"),
    path('student/login/', views.student_login, name="Student login"),
    path('student/logout/', views.logout_view, name='logout'),
    path('student/dashboard/', views.dashboard, name="Student Dashboard"),
    path('student/profile/<std_number>', views.profile, name="Student Profile"),
    path('student/paymenthistory/<std_number>', views.paymenthistory, name="Payment History"),
    path('student/my_results/<std_number>/<class_id>', views.my_results, name="My results"),
]