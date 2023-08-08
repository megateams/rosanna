
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
    path('finance/', views.financedashboard, name=""),

    path('financeaddfees/', views.financeaddFees, name="Add Fees"),
    path('financefeeslist/', views.financefeesList, name="Fees List"),

    path('financeaddfeesstructure/', views.financeaddFeesstructure, name="Add Fees Structure"),
    path('financefeesstructurelist/', views.financefeesstructureList, name="Fees Structure List"),
   
   path('financeaddexpenses/', views.financeaddExpenses, name="Add Expenses"),
    path('financeexpenseslist/', views.financeexpensesList, name="Expenses List"),

    path('financeaddstaffpayments/', views.financeaddStaffpayments, name="Add Staffpayments"),
    path('financestaffpaymentslist/', views.financestaffpaymentsList, name="Staffpayments List"),

    path('financereports/', views.financeReports, name =" Reports"),
    path('financestatistics/', views.financeStatistics, name =" Statistics"),
]
