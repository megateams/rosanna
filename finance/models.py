from django.db import models
from frontend.models import Teachers 

# Create your models here.
        
class Staffpayments(models.Model):
    staffid = models.ForeignKey(Teachers , on_delete=models.CASCADE)
    staffname = models.CharField(max_length=25 , verbose_name='Staff Name' , blank=True)
    datepaid = models.DateField(verbose_name='Payment Date' , blank=True)
    salary = models.IntegerField(verbose_name='Salary' , blank=True)
    amountpaid = models.IntegerField(verbose_name='Amount Paid' , blank=True)
    balance = models.IntegerField(verbose_name='Balance' , blank=True)
    position = models.CharField(max_length=15 , verbose_name='Position' , blank=True)
    bankaccnum = models.IntegerField(verbose_name='Account Number' , blank=True)

    displaystaffpayments = [
        'staffname' , 'datepaid' , 'salary' , 'amountpaid' , 'balance' , 'position' , 'bankaccnum'
    ]

class Bankdetails(models.Model):
    staffname = models.CharField(max_length=20 , verbose_name='Staff Names' , blank=True)
    bankname = models.CharField(max_length=30 ,  verbose_name='Bank Name' , blank=True)
    accnum = models.IntegerField(verbose_name='Account Number' , blank=True)
    accname = models.CharField(verbose_name='Account Name' , max_length=25 , blank=True)
    
    displaybankdetails = [
        'staffname' , 'bankname' , 'accnum' , 'accname'
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
    
    displayreceipts = [
        'receiptnum' , 'transactiondate' , 'amountpaid' , 'item' , 'balance' , 'payername'
    ]
    

















