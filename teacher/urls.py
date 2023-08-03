
from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.dashboard, name=""),
    path('teacherprofile/', views.profile, name="Teacher Profile"),
    path('paymenthistory/', views.paymenthistory, name="Payment History"),
]