
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

    path('fees/', views.Fees, name="Fees"),
    path('finance/', views.financedashboard, name=""),
    path('financeaddfees/', views.financeaddFees, name="Add Fees"),

    path('financefeeslist/', views.financefeesList, name="financefeeslist"),
    path('financefeeslist/', views.financefeesList, name="Fees List"),

    path('financeaddfeesstructure/', views.financeaddFeesstructure, name="Add Fees Structure"),
    path('financefeesstructurelist/', views.financefeesstructureList, name="Fees Structure List"),
    path('editfeesstructure/<int:feesstructureid>/', views.editfeesstructure, name='editfeesstructure'),
    path('deletefeesstructure/<int:feesstructureid>/', views.deletefeesstructure, name='deletefeesstructure'),

   
    path('financeaddexpenses/', views.financeaddExpenses, name="Add Expenses"),
    path('financeexpenseslist/', views.financeexpensesList, name="Expenses List"),
    path('delete_expense/<str:expenseid>/', views.delete_expense, name='delete_expense'),
    path('edit_expense/<str:expenseid>/', views.edit_expense, name='edit_expense'),

    path('financeaddstaffpayments/', views.financeaddStaffpayments, name="Add Staffpayments"),
    #path('financestaffpaymentslist/', views.financestaffpaymentsList, name="Staffpayments List"),
    path('financeaddteacherpayments/', views.financeaddTeacherpayments, name="Add Teacherpayments"),
    path('financeteacherpaymentslist/', views.financeteacherpaymentsList, name="teacherpaymentslist"),
    path('financeteacherpaymentslist/deleteteacherpayment/<id>' , views.deleteteacherpayment , name = 'deleteteacherpayments'),

    path('financeaddsupportstaffpayments/', views.financeaddsupportstaffpayments, name="Add Supportstaffpayments"),
    path('financesupportstaffpaymentslist/', views.financesupportstaffpaymentsList, name="SupportstaffpaymentsList"),
    path('financereports/', views.financeReports, name =" Reports"),
    path('financestatistics/', views.financeStatistics, name =" Statistics"),

    
    path('financesupportstaffpaymentslist/deletesupportstaffpayment/<paymentid>' , views.deletesupportstaffpayment , name='deletesupportstaffpayments'),

    path('get_stdclass/<stdnumber>/', views.get_stdclass, name =" Get Student class"),
    path('financesupportstaffpaymentslist/editsupportstaffpayment/<paymentid>' , views.editsupportstaffpayment , name = "editsupportstaffpayments"),
    path('editsupportstaffpayments' , views.editsupportstaffpayment , name = 'editsupportstafpaymentsform'),
    
    path('financeteacherpaymentslist/editteacherpayment/<id>' , views.editteacherpayments , name = 'editteacherpayment')
]
