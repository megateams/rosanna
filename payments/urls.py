
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('payments/', views.paymentslogin , name='paymentsloginpage'), 
    path('paymentsdashboard/', views.paymentsdashboard, name="Payments Dashboard"),

    path('getsupportstaffbalance/<id>/<amountpaid>/' , views.getsupportstaffbalance, name = 'getsupportstaffbalance'),
 
    path('that_term/<id>', views.that_term, name="that_term"), 
    
    path('financeaddteacherpayments/', views.financeaddTeacherpayments, name="AddTeacherpayments"),
    path('financeteacherpaymentslist/', views.financeteacherpaymentsList, name="teacherpaymentslists"),
    path('financeaddsupportstaffpayments/', views.financeaddsupportstaffpayments, name="Add Supportstaffpayments"),
    path('financesupportstaffpaymentslist/', views.financesupportstaffpaymentsList, name="SupportstaffpaymentsLists"), 
    path('deletesupportstaffpayment/' , views.deletesupportstaffpayment , name='deletesupportstaffpayments'),
    path('deleteteacherpayment/' , views.deleteteacherpayment , name='deleteteacherpayments'),
    path('financesupportstaffpaymentslist/editsupportstaffpayment/<paymentid>' , views.editsupportstaffpayment , name = "editsupportstaffpayments"),
    path('editsupportstaffpayments/' , views.editsupportstaffpayment , name = 'editsupportstafpaymentsform'),
    path('editteacherpayments/' , views.editteacherpayments , name = 'editteacherpayments'),
    path('financeteacherpaymentslist/editteacherpayment/<id>' , views.editteacherpayments , name = 'editteacherpayment'),
    path('get_staff_salary/<id>/' , views.get_staff_salary , name = 'get_staff_salary'),
    path('get_teacher_salary/<id>/' , views.get_teacher_salary , name = 'get_teacher_salary'),
    path('get_teacher_balance/<id>/<amountpaid>/' , views.get_teacher_balance , name = 'get_teacher_balance'),

    path('export_teacher_payments/', views.export_teacher_payments_to_excel, name='export_teacher_payments'),
    path('export_support_staffpayments/', views.export_support_staff_payments_to_excel, name='export_support_staff_payments'),

] 
