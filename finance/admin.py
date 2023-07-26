from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display =Fees.Display_Fees
    
@admin.register(ExpenseRecord)
class ExpenseRecord(admin.ModelAdmin):
    list_display =ExpenseRecord.Display_ExpenseRecords
    