from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import save_registration

urlpatterns = [
    # Login and Logout URLs
    # path("login/", auth_views.LoginView.as_view(template_name="frontend/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    # path('', views.login, name="Login"),
    path('dashboard/', views.home, name="Dashboard"),

    path('students/', views.students, name="Students"),
    # path('save_registration/', save_registration, name='save_registration')
    path('studentslist/', views.studentsList, name="Studentslist"),
    path('addstudent/', views.studentsAdd, name="AddStudents"),
    #path('addstudent/submit/', views.studentReg, name="studentReg"),
    path('addstudent/', views.studentsAdd, name="Add Students"),
    path('export-excel', views.export_to_excel, name="export_excel"),
    path('deletestudent/<stdnumber>', views.DeleteStudent, name="deleteStudent"),
    #path('countstudent/', views.Count_Student, name="count_student"),
    path('addstudent/submit/', views.studentReg, name="studentReg"),
    # path('addstudent/', views.studentsAdd, name="Add Students"),
    path('addteacher/', views.teacherAdd, name="Add Teacher"),
    path('teacherlist/', views.teacherList, name="Teachers List"),
    path('addteacher/submit/', views.teachers, name="Teachers"),
    path('edit_teacher/', views.edit_teacher, name="edit_teacher"),
    path('teacher_export/', views.teacher_export_to_excel, name="teacher_export"),

    path('addusers/', views.addUsers, name="Add User"),
    path('userslist/', views.usersList, name="View List"),

    # path('addmarks/', views.addMarks, name="Add Marks"),
    path('markslist/', views.marksList, name=" View Marks"),    

    # path('addsubject/', views.addSubject, name="Add Subject"),
    path('subjectlist/', views.subjectList, name="Subjects List"),

    path('addmarks/submitmarks/', views.submitmarks, name="Submit Marks"),
    path('addmarks/', views.addmarks, name="Add Marks"),
    path('markslist/', views.marksList, name="viewmarks"),    

    #path('showstudent/', views.showStudent, name="Student details"),
    path('addmarks/', views.addMarks, name="Add Marks"),
    path('markslist/', views.marksList, name=" View Marks"),  
    path('get_subjects/<int:class_id>/', views.get_subjects, name='get_subjects'),  
    path('showstudent/<stdnumber>', views.showStudent, name="Student details"),
    path('get_students_by_class/<int:class_id>/', views.get_students_by_class, name='get_students_by_class'),
    path('support-staff-list/', views.supportstaffList, name="Support staff List"),
    path('add-support-staff/', views.supportstaffAdd, name="AddSupportstaff"),
    path('showteacher/<teacherId>', views.showteacher, name="Show Teacher"),
    path('add-support-staff/submit/', views.supportstaffreg, name='supportstaffreg'),
    path('support-export-excel/', views.support_staff_export_to_excel, name='support_export_excel'),
    path('deletesupportstaff/<int:id>', views.DeleteSupportStaff, name ="deleteSupportStaff"),
    path('markslist/deletemarks/<id>' , views.deletemarks , name='deletemarks'),
    path('supportstafflistview/', views.Support_Staff_list_View, name ="supportstafflistview"),
    # path('add-support-staff/', views.supportstaffreg, name='supportstaffreg'),
    path('staff/', views.staff, name="Staff"),
    path('addsubjectsform/' , views.addsubjectsform , name = "addsubjectsform"),
    path('addsubject/' , views.addsubject , name = 'addsubject'),
    path('assign_subjecthead/' , views.assign_subjecthead , name = 'assign_subjecthead'),
    path('edit_subject/' , views.edit_subject , name = 'edit_subject'),
    path('delete_subject/' , views.delete_subject , name = 'delete_subject'),
    path('showclasses/' , views.showclasses , name='showclasses'),
    path('sendclasses/' , views.schoolclasses , name = 'schoolclasses'),

    # path('showclasses/addclasses/' , views.addclasses , name='showclassesaddclass'),
    path('subjectlist/delete_subject/<subjectid>' , views.deletesubject , name='deletesubject'),
    path('showclasses/delete_class/<classid>' , views.deleteclass , name='deleteclass'),

    # path('showclasses/addclasses/' , views.addclasses , name='AddClasses'),
    path('addclasses/sendclasses/' , views.schoolclasses , name = 'schoolclasses'),
    path('addclasses/' , views.addclasses , name='AddClasses'),
    path('edit_class/' , views.edit_class , name='edit_class'),
    path('delete_class/' , views.delete_class , name='delete_class'),

    # accounting 
    path('feesstructurelist/', views.feesstructure, name='Fees Structure'),
    path('feeslist/', views.fees, name='Fees '),
    path('teacherspaymentslist/', views.teacherspayments, name='Teachers Payments '),
    path('supportstaffpaymentslist/', views.supportstaffpayments, name='Supportstaff Payments '),
    path('expenseslist/', views.expenses, name='Expenses '),
]