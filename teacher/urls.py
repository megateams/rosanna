
from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.login, name="teacherloginpage"),
    path('teacher/login/', views.teacher_login, name="Teacher login"),
    path('teacher/logout/', views.logout_view, name='logout'),
    path('teacher/dashboard/', views.dashboard, name="Teacher Dashboard"),
    path('teacher/profile/<teacher_id>', views.profile, name="Teacher Profile"),
    path('teacher/paymenthistory/<teacher_id>', views.paymenthistory, name="Payment History"),

    # marks urls
    path('teacher/his_class/addmarks/<class_id>/<teacher_id>', views.addmarks, name="Add Marks"),
    path('submit_marks/<class_id>/<teacher_id>/', views.submit_marks, name="Submit Marks"),
    path('submit_subject_marks/<class_id>/<teacher_id>/<subject_id>/', views.submit_subject_marks, name="Submit Marks"),
    path('teacher/his_class/view_marks/<class_id>/<teacher_id>', views.view_marks, name="View Marks"),
    path('teacher/his_class/view_mark/<int:class_id>/<str:teacher_id>/', views.view_marks_by_marktype, name='view_marks_by_marktype'),
    path('teacher/class_marks/<int:class_id>/<str:teacher_id>/', views.class_marks_by_marktype, name='class_marks_by_marktype'),
    
    path('get_students_by_class/<int:class_id>/', views.get_students_by_class, name='get_students_by_class'),
    path('get_subjects/<int:class_id>/', views.get_subjects, name='get_subjects'), 
    path('enroll_student/<classid>/<teacher_id>', views.enroll_student, name='enroll_student'), 
    path('enrollment_history/<classid>/<teacher_id>', views.enrollment_history, name='enrollment_history'), 

    # class details url
    path('teacher/class_details/<int:class_id>/<teacher_id>', views.class_details, name='Class Details'),
    path('teacher/his_class/<int:class_id>/<teacher_id>', views.his_class, name='his_class'),
    path('teacher/class_details/addmarks/<int:class_id>/<teacher_id>/<subject_id>', views.addsubjectmarks, name= 'Add Subject marks'),

    # generate report card
    path('report_card/<student_id>/<position>', views.generate_report, name='Student report card'),
    path('teacher/profile/edit-profile/<teacher_id>', views.edit_teacher_profile, name='Edit Teacher Profile'),
    path('teacher/edit_all_marks', views.edit_all_marks, name='edit_all_marks'),    
    path('get_mark/<str:student_id>/<str:subject_id>/<str:mark_type>/', views.get_mark, name='get_mark'),
    path('teacher/assign_subject/', views.assign_subject, name='assign_subject'),
    path('teacher/assign_subject/', views.assign_subject, name='assign_subject'),
    path('set_promotion_mark/<class_id>/<teacher_id>/', views.set_promotion_mark, name='set_promotion_mark'),


]












