from django.db import models
from frontend.models import Student
# Create your models here.
CLASS_CHOICES =[
    ('baby' , 'baby'),
    ('middle' , 'middle'),
    ('top' , 'top'),
    ('P.1' , 'P.1'),
    ('P.2' , 'P.2'),
    ('P.3' , 'P.3'),
    ('P.4' , 'P.4'),
    ('P.5' , 'P.5'),
    ('P.6' , 'P.6'),
    ('P.7' , 'P.7')
]
class Fees(models.Model):
    paymentid =models.CharField(max_length= 50, primary_key=True, verbose_name= "Pyament ID")
    stdnumber = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student ID")
    stdname = models.CharField(max_length=255, blank =True, verbose_name="Student name")
    studentclass = models.CharField(choices=CLASS_CHOICES , max_length=6 , verbose_name='Class' , blank=True)
    amount = models.CharField(max_length= 20, verbose_name='Amount paid' , blank=True)
    balance = models.CharField(max_length=20 , verbose_name='Balance' , blank=True)
    modeofpayment =models.CharField(max_length=255, blank=True, verbose_name="Mode of Payment")
    date =models.DateField(verbose_name="Date of Payment")
    
    Display_Fees =['paymentid', 'stdnumber', 'stdname', 'studentclass', 'amount', 'balance', 'modeofpayment', 'date']
    
class ExpenseRecord(models.Model):
    expenseid =models.CharField( max_length =50, primary_key=True, verbose_name="Expense ID")
    category =models.CharField(max_length=255, blank=True, verbose_name="Expense category")
    amountrequired =models.CharField(max_length=20, blank=True, verbose_name="Amount required")
    expensedate =models.DateField(verbose_name="Date of Expense")
    amountpaid =models.CharField(max_length=20, blank=True, verbose_name="Amount paid")
    balance =models.CharField(max_length=20, blank=True, verbose_name="Balance")
    
    Display_ExpenseRecords =['expenseid', 'category', 'amountrequired', 'expensedate', 'amountpaid', 'balance']

    
