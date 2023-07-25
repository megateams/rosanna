from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Staffpayments)
class Displaystaffpayments(admin.ModelAdmin):
    list_display = models.Staffpayments.displaystaffpayments

@admin.register(models.Receipts)
class Displayreceipts(admin.ModelAdmin):
    list_display = models.Receipts.displayreceipts

@admin.register(models.Bankdetails)
class Displaybankdetails(admin.ModelAdmin):
    list_display = models.Bankdetails.displaybankdetails






