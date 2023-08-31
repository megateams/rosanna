from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display =Fees.Display_Fees
    
@admin.register(ExpenseRecord)
class ExpenseRecord(admin.ModelAdmin):
    list_display =ExpenseRecord.Display_ExpenseRecords

# Register your models here.

@admin.register(Staffpayments)
class Displaystaffpayments(admin.ModelAdmin):
    list_display = Staffpayments.displaystaffpayments

@admin.register(Receipts)
class Displayreceipts(admin.ModelAdmin):
    list_display = Receipts.displayreceipts

@admin.register(Bankdetails)
class Displaybankdetails(admin.ModelAdmin):
    list_display = Bankdetails.displaybankdetails
