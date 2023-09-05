from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import save_registration

urlpatterns = [
    path('deleteadmin/' , views.deleteadmin , name = "deleteadmin"),
    path('editadministrator/' , views.editadministrator , name = 'editadministrator'),
    path("", views.user_login, name="Admin Login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("register/", views.register, name="register"),
    path('dashboard/', views.home, name="Dashboard"),

    # path('save_registration/', save_registration, name='save_registration')
    path('studentslist/', views.studentsList, name="Students List"),
    path('student-by-class/<int:class_id>/', views.student_by_class, name='student_by_class'),
    path('addstudent/', views.studentsAdd, name="AddStudents"),
    path('addstudent/submit/', views.studentReg, name="studentReg"),
    path('edit_student/', views.edit_student, name="edit_student"),
    path('delete_student/', views.delete_student, name="delete_student"),
    path('edit_std_image/', views.edit_std_image, name="edit_std_image"),
    path('edit_tr_image/', views.edit_tr_image, name="edit_tr_image"),

    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),
    path('addteacher/submit/', views.teachers, name="Teachers"),
    
    path('addadmins/' , views.addadmins , name='submitadmins'),
    path('adminslist/' , views.adminslist , name = 'adminslist'),
    
    path('edit_teacher/', views.edit_teacher, name="edit_teacher"),
    path('delete_teacher/', views.delete_teacher, name="delete_teacher"),
    path('teacher_export/', views.teacher_export_to_excel, name="teacher_export"),

    path('addusers/', views.addUsers, name="Add User"),
    path('userslist/', views.usersList, name="View List"),
    path('markslist/', views.marksList, name=" View Marks"),    

    # path('addmarks/submitmarks/', views.submitmarks, name="Submit Marks"),   

    path('addmarks/', views.addMarks, name="Add Marks"),
    path('markslist/', views.marksList, name=" View Marks"),  
    path('view_marks/<int:class_id>/', views.view_marks, name=" view_marks"),  
    path('view_mark/<int:class_id>/', views.view_marks_by_type, name=" view_marks_by_type"),  
    path('get_subjects/<int:class_id>/', views.get_subjects, name='get_subjects'),  

    path('showstudent/<stdnumber>', views.showStudent, name="Student details"),
    path('get_students_by_class/<int:class_id>/', views.get_students_by_class, name='get_students_by_class'),


    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="AddSupportstaff"),
    path('showteacher/<teacherId>', views.showteacher, name="Show Teacher"),
    path('add-support-staff/submit/', views.supportstaffreg, name='supportstaffreg'),
    # path('add-support-staff/', views.supportstaffreg, name='supportstaffreg'),
    path('showsupportstaff/<int:supportstaffid>/', views.showsupportstaff, name='show supportstaff'),
    path('edit_supportstaff/', views.edit_supportstaff, name="edit_supportstaff"),
    path('delete_supportstaff/', views.delete_supportstaff, name="delete_supportstaff"),


    path('addsubjectsform/' , views.addsubjectsform , name = "addsubjectsform"),
    path('addsubject/' , views.addsubject , name = 'addsubject'),
    path('assign_subjecthead/' , views.assign_subjecthead , name = 'assign_subjecthead'),
    path('edit_subject/' , views.edit_subject , name = 'edit_subject'),
    path('delete_subject/' , views.delete_subject , name = 'delete_subject'),
    path('showclasses/' , views.showclasses , name='showclasses'),
    path('sendclasses/' , views.schoolclasses , name = 'schoolclasses'),

    path('subjectlist/' , views.subjectList , name = 'subjectList'),



    # path('showclasses/addclasses/' , views.addclasses , name='showclassesaddclass'),
    # path('subjectlist/delete_subject/<subjectid>' , views.deletesubject , name='deletesubject'),
    # path('showclasses/delete_class/<classid>' , views.deleteclass , name='deleteclass'),

    path('addclasses/sendclasses/' , views.schoolclasses , name = 'schoolclasses'),
    path('addclasses/' , views.addclasses , name='AddClasses'),
    path('edit_class/' , views.edit_class , name='edit_class'),
    path('delete_class/' , views.delete_class , name='delete_class'),

    # accounting 
    path('feesstructurelist/', views.feesstructure, name='Fees Structure'),
    path('feeslist/', views.fees, name='Fees '),
    path('fees_by_class/<int:class_id>/', views.fees_by_class, name='fees_by_class'),
    #path('teacherspaymentslist/', views.teacherspayments, name='Teachers Payments '),
    #path('supportstaffpaymentslist/', views.supportstaffpayments, name='Supportstaff Payments '),
    path('expenseslist/', views.expenses, name='Expenses '),
    
    path('supportstaffpaymentslist/', views.supportstaffpaymentsList, name="SupportstaffpaymentsLists"),
    path('teacherpaymentslist/', views.financeteacherpaymentsList, name="teacherpaymentslists"),

   path('export_subjects/', views.export_subjects_to_excel, name='export_subjects'),
   path('export_classes/', views.export_classes_to_excel, name='export_classes'),


    # settings urls
   path('settings/enrollment/', views.settings, name='settings'),
   path('settings/school_info/', views.school_info, name='School Information'),
   path('edit_term/', views.edit_term, name='edit_term'),
   path('delete_term/', views.delete_term, name='delete_term'),

#    imports
    # path('import_excel/', views.import_excel, name='import_excel'),




]















