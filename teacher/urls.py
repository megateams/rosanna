
from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.dashboard, name="Dashboard"),
]