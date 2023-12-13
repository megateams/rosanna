
"""
URL configuration for rosanna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('finance/', views.financelogin , name='financeloginpage'),
    path('financedashboard/', views.financedashboard, name="Finance Dashboard"), 
    
    path('bursar_profile/', views.bursar_profile, name='bursar_profile'),
    path('edit_bursar_profile/', views.edit_bursar_profile, name='edit_bursar_profile'),

    path('that_term/<id>', views.that_term, name="that_term"), 
    
    path('students/', views.students_list, name='students_list'),

    path('finance/students_by_class/<int:class_id>/', views.students_by_class, name='students_by_class'),
    path('assign_code/<str:stdnumber>/', views.assign_school_code, name='assign_school_code'),
    path('financeaddfees/', views.financeaddFees, name="Add Fees"),
    path('financefeeslist/', views.financefeesList, name="Fees List"),
    path('finance/fees_by_class/<int:class_id>/', views.fees_by_class, name='fees_by_class'),
    path('delete_fee/', views.delete_fee, name='delete_fee'),
    path('edit_std_fees/', views.edit_std_fees, name='edit_std_fees'),
    path('feesclearedstudents/', views.feesclearedstudents, name='Cleared Students List'),
    path('feesclearedstudents_byclass/<int:class_id>/', views.feesclearedstudents_byclass, name='Cleared Students by Class'),
    path('generate_clearance/<str:stdnumber>/', views.generate_clearance, name='Generate Clearance'),
    path('clearance_card/<str:stdnumber>/', views.clearance_card, name='Clearance Card'),

    path('financeaddfeesstructure/', views.financeaddFeesstructure, name="Add Fees Structure"),
    path('financefeesstructurelist/', views.financefeesstructureList, name="Fees Structure List"),
    path('editfeesstructure/<int:feesstructureid>/', views.editfeesstructure, name='editfeesstructure'),
    path('deletefeesstructure/<int:feesstructureid>/', views.deletefeesstructure, name='deletefeesstructure'),

    path('financeaddutilities/', views.financeaddUtilities, name="Add Utilities"),
    path('financeutilitieslist/', views.financeutilitiesList, name="Utilities List"),
    path('delete_utilities/', views.delete_utilities, name='delete_utilities'),
    path('edit_utilities/<str:utilitiesid>/', views.edit_utilities, name='edit_utilities'),
    path('financereports/', views.financeReports, name =" Reports"),
    path('financestatistics/', views.financeStatistics, name =" Statistics"),

    path('export_financefees/', views.export_finance_fees_to_excel, name='export_finance_fees_to_excel'),
    path('export-fees-by-class/<int:class_id>/', views.export_fees_by_class, name='export_fees_by_class'),
    path('export-feesstructure/', views.export_fees_structure_to_excel, name='export_fees_structure_to_excel'),
    path('export_utilities/', views.export_utilities_to_excel, name='export_utilities'),
    path('export_clearedstudents_to_excel/', views.export_clearedstudents_to_excel, name='Export Cleared Students to Excel'),

    # reports
    path('feesreport/', views.feesReport, name="Fees Report"),
    path('finance/feesreport_by_class/<int:class_id>/', views.feesreport_by_class, name='feesreport_by_class'),


]
