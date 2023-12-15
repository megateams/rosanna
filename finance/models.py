from django.db import models
from frontend.models import *
from django.utils import timezone
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

# feesstructure models
class Feesstructure(models.Model):
    feesstructureid = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=20)
    amount = models.IntegerField()
    term = models.CharField(max_length=10, default=None)
    year = models.PositiveIntegerField(default=None) 
# feesstructure models

class Fees(models.Model):
    paymentid = models.AutoField(primary_key=True)
    stdnumber = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student ID")
    stdname = models.CharField(max_length=255, blank =True, verbose_name="Student name")
    studentclass = models.CharField(choices=CLASS_CHOICES , max_length=20 , verbose_name='Class' , blank=True)
    classfees = models.CharField(max_length= 20, verbose_name='Class Fees' , blank=True)
    amount = models.CharField(max_length= 20, verbose_name='Amount paid' , blank=True)
    # accumulatedpayment = models.IntegerField(verbose_name = 'Accumulated Amount' , default = None)
    accumulatedpayment = models.IntegerField(default=0)
    balance = models.IntegerField(verbose_name='Balance' , blank=True)
    modeofpayment =models.CharField(max_length=255, blank=True, verbose_name="Mode of Payment")
    date =models.DateTimeField(auto_now=True)
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None, null=True)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None, null=True)
    
    Display_Fees =['paymentid', 'stdnumber', 'stdname', 'studentclass', 'amount', 'balance', 'modeofpayment', 'date', 'term', 'year']
    
class Utilities(models.Model):
    utilitiesid = models.AutoField(primary_key=True)
    category =models.CharField(max_length=255, blank=True, verbose_name="Utility category")
    utilitiesdate =models.DateField(verbose_name="Date of Utilities")
    amountpaid =models.CharField(max_length=20, blank=True, verbose_name="Amount paid")
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    
    Display_Utilities =['utilitiesid', 'category', 'utilitiesdate', 'amountpaid', 'term', 'year']

class Supplementaryincome(models.Model):
    supplementaryincomeid = models.AutoField(primary_key=True)
    category =models.CharField(max_length=255, blank=True, verbose_name="Category")
    date =models.DateField(verbose_name="Date")
    amount =models.CharField(max_length=20, blank=True, verbose_name="Amount")
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    
    Display_Supplementaryincome =['supplemetaryincomeid', 'category', 'date', 'amount', 'term', 'year']



# Create your models here.
        
class Staffpayments(models.Model):
    staffid = models.ForeignKey(Teachers , on_delete=models.CASCADE)
    staffname = models.CharField(max_length=25 , verbose_name='Staff Name' , blank=True)
    datepaid = models.DateField(verbose_name='Payment Date' , blank=True)
    salary = models.IntegerField(verbose_name='Salary' , blank=True)
    amountpaid = models.IntegerField(verbose_name='Amount Paid' , blank=True)
    balance = models.IntegerField(verbose_name='Balance' , blank=True)
    position = models.CharField(max_length=15 , verbose_name='Position' , blank=True)
    bankaccnum = models.IntegerField(verbose_name='Account Number' , blank=True , default=None)
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    displaystaffpayments = [
        'staffname' , 'datepaid' , 'salary' , 'amountpaid' , 'balance' , 'position' , 'bankaccnum', 'term', 'year'
    ]

class Bankdetails(models.Model):
    staffname = models.CharField(max_length=20 , verbose_name='Staff Names' , blank=True)
    bankname = models.CharField(max_length=30 ,  verbose_name='Bank Name' , blank=True)
    accnum = models.IntegerField(verbose_name='Account Number' , blank=True)
    accname = models.CharField(verbose_name='Account Name' , max_length=25 , blank=True)
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    
    displaybankdetails = [
        'staffname' , 'bankname' , 'accnum' , 'accname', 'term', 'year'
    ]
    
class Receipts(models.Model):
    recipts_staffpayments_relationship = models.ForeignKey(Staffpayments , on_delete=models.CASCADE)
    receipts_staff_relationship = models.ForeignKey(Teachers , on_delete=models.CASCADE)
    
    receiptnum = models.CharField(primary_key=True , max_length=20 , verbose_name='Receipt Number' , blank=True)
    transactiondate = models.DateField(verbose_name= 'Transaction Date' , blank=True)
    amountpaid = models.IntegerField(verbose_name='Amount Paid' , blank=True)
    item = models.CharField(max_length=30 , verbose_name='Item' , blank=True)
    balance = models.IntegerField(verbose_name='Balance' , blank=True)
    payername = models.CharField(max_length=30 , verbose_name='Payer Name' , blank=True)
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    
    displayreceipts = [
        'receiptnum' , 'transactiondate' , 'amountpaid' , 'item' , 'balance' , 'payername', 'term', 'year'
    ]
    
class Teacherspayment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    teacherid = models.CharField(max_length=20 , verbose_name='Teacher id')
    teachername = models.CharField(max_length=30 , verbose_name='Teacher Name' , default=None) 
    paymentdate = models.DateField(verbose_name='Payment Date')
    salary = models.IntegerField(verbose_name='Salary')
    amountpaid = models.IntegerField(verbose_name='Amount Paid')
    accumulatedpayment = models.IntegerField(verbose_name = 'Accumulated Amount' , default = None)
    balance = models.IntegerField(verbose_name='Balance')
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    
    displayteacherpayment = [
        'paymentid' , 'paymentdate' , 'salary' , 'amountpaid' , 'accumulatedamount' , 'balance' , 'paymentmethod' , 'bankaccnum', 'term', 'year'
    ]
    
    
class Supportstaffpayment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    supportstaffid = models.CharField(max_length=10 , verbose_name='Support Staff id')
    staffname = models.CharField(max_length = 25 , verbose_name='Staffname' , null=True)
    salary = models.IntegerField(verbose_name='Salary')
    amountpaid = models.IntegerField(verbose_name='Amount Paid')
    paymentdate = models.DateField(max_length=6 , verbose_name='PAyment Date' , null=True)
    balance = models.IntegerField(verbose_name='Balance')
    accumulatedamount = models.IntegerField(verbose_name='Accumulated Amount' , default=None)
    term = models.CharField(max_length=10, blank=True, verbose_name="Term", default=None)
    year = models.PositiveIntegerField(blank=True, verbose_name="Year", default=None)
    
    displaysupportstaffpayment = [
        'supportstaffid','paymentid' , 'paymentdate' , 'salary' , 'amountpaid' , 'balance', 'term', 'year'
    ]











