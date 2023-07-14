from django.contrib import admin
from .models import Registration

# Register your models here.

@admin.register(Registration)
class MyClass(admin.ModelAdmin):
    list_display = Registration.Display_Fields





