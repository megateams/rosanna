
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
    path('teacher/his_class/addmarks/<class_id>/<teacher_id>', views.addmarks, name="Add Marks"),
    path('teacher/his_class/view_marks/<class_id>/<teacher_id>', views.view_marks, name="View Marks"),
    path('teacher/his_class/view_mark/<int:class_id>/<str:teacher_id>/', views.view_marks_by_marktype, name='view_marks_by_marktype'),
    
    path('get_students_by_class/<int:class_id>/', views.get_students_by_class, name='get_students_by_class'),
    path('get_subjects/<int:class_id>/', views.get_subjects, name='get_subjects'), 

    # class details url
    path('teacher/class_details/<int:class_id>/<teacher_id>', views.class_details, name='Class Details'),
    path('teacher/his_class/<int:class_id>/<teacher_id>', views.his_class, name=''),
    path('teacher/class_details/addmarks/<int:class_id>/<teacher_id>/<subject_id>', views.addsubjectmarks, name= 'Add Subject marks'),

    # generate report card
    path('teacher/report_card/<student_id>', views.generate_report, name='Student report card'),
]