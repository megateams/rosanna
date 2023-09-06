
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
    
    path('financeaddfees/', views.financeaddFees, name="Add Fees"),
    path('financefeeslist/', views.financefeesList, name="Fees List"),
    path('fees_by_class/<int:class_id>/', views.fees_by_class, name='fees_by_class'),
    path('delete_fee/', views.delete_fee, name='delete_fee'),
    path('edit_std_fees/', views.edit_std_fees, name='edit_std_fees'),

    path('financeaddfeesstructure/', views.financeaddFeesstructure, name="Add Fees Structure"),
    path('financefeesstructurelist/', views.financefeesstructureList, name="Fees Structure List"),
    path('editfeesstructure/<int:feesstructureid>/', views.editfeesstructure, name='editfeesstructure'),
    path('deletefeesstructure/<int:feesstructureid>/', views.deletefeesstructure, name='deletefeesstructure'),

   
    path('financeaddexpenses/', views.financeaddExpenses, name="Add Expenses"),
    path('financeexpenseslist/', views.financeexpensesList, name="Expenses List"),
    path('delete_expense/', views.delete_expense, name='delete_expense'),
    path('edit_expense/<str:expenseid>/', views.edit_expense, name='edit_expense'),

    path('financeaddteacherpayments/', views.financeaddTeacherpayments, name="AddTeacherpayments"),

    path('financeteacherpaymentslist/', views.financeteacherpaymentsList, name="teacherpaymentslists"),

    path('financeaddsupportstaffpayments/', views.financeaddsupportstaffpayments, name="Add Supportstaffpayments"),
    path('financesupportstaffpaymentslist/', views.financesupportstaffpaymentsList, name="SupportstaffpaymentsLists"),
    path('financereports/', views.financeReports, name =" Reports"),
    path('financestatistics/', views.financeStatistics, name =" Statistics"),

    
    path('deletesupportstaffpayment/' , views.deletesupportstaffpayment , name='deletesupportstaffpayments'),
    path('deleteteacherpayment/' , views.deleteteacherpayment , name='deleteteacherpayments'),

    path('get_stdclass/<stdnumber>/', views.get_stdclass, name =" Get Student class"),
    path('financesupportstaffpaymentslist/editsupportstaffpayment/<paymentid>' , views.editsupportstaffpayment , name = "editsupportstaffpayments"),
    path('editsupportstaffpayments/' , views.editsupportstaffpayment , name = 'editsupportstafpaymentsform'),
    path('editteacherpayments/' , views.editteacherpayments , name = 'editteacherpayments'),

    path('financeteacherpaymentslist/editteacherpayment/<id>' , views.editteacherpayments , name = 'editteacherpayment'),
    path('get_staff_salary/<id>/' , views.get_staff_salary , name = 'get_staff_salary'),
    path('get_teacher_salary/<id>/' , views.get_teacher_salary , name = 'get_teacher_salary'),
    path('get_teacher_balance/<id>/<amountpaid>/' , views.get_teacher_balance , name = 'get_teacher_balance'),

    # path('export_excel/', views.export_to_excel, name='export_excel'),
    path('export_financefees/', views.export_finance_fees_to_excel, name='export_finance_fees_to_excel'),
    path('export-feesstructure/', views.export_fees_structure_to_excel, name='export_fees_structure_to_excel'),
    path('export_expenses/', views.export_expenses_to_excel, name='export_expenses'),
    path('export_teacher_payments/', views.export_teacher_payments_to_excel, name='export_teacher_payments'),
    path('export_support_staffpayments/', views.export_support_staff_payments_to_excel, name='export_support_staff_payments'),

]
