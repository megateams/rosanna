
from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.login, name="Login Page"),
    path('teacher/login/', views.teacher_login, name="Teacher login"),
    path('teacher/logout/', views.logout_view, name='logout'),
    path('teacher/dashboard/', views.dashboard, name="Teacher Dashboard"),
    path('teacher/profile/<teacher_id>', views.profile, name="Teacher Profile"),
    path('teacher/paymenthistory/', views.paymenthistory, name="Payment History"),

    # marks urls
    path('teacher/marks/', views.addmarks, name="Add Marks"),
    path('get_students_by_class/<int:class_id>/', views.get_students_by_class, name='get_students_by_class'),
    path('get_subjects/<int:class_id>/', views.get_subjects, name='get_subjects'), 

    # class details url
    path('teacher/class_details/<int:class_id>/<teacher_id>', views.class_details, name='Class Details'),
    path('teacher/class_details/addmarks/<int:class_id>/<teacher_id>/<subject_id>', views.addsubjectmarks, name= 'Add Subject marks'),
]