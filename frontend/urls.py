from django.urls import path
from . import views
# from .views import save_registration

urlpatterns = [
    path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),
    path('students/', views.students, name="Students"),
    path('test/', views.test, name="test"),
    # path('save_registration/', save_registration, name='save_registration')
]