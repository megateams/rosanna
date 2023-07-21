from django.contrib import admin
from .models import Login, Admin_Model, Role_Model, Supportstaff

# Register your models here.
# admin.site.register(Registration)
# admin.site.register(Login)

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display =Login.Display_Login_Fields

@admin.register(Admin_Model)
class Admin_ModelAdmin(admin.ModelAdmin):
    list_display=Admin_Model.Display_Admins
    
@admin.register(Role_Model)
class Role_modelAdmin(admin.ModelAdmin):
    list_display=Role_Model.Display_Roles
    
@admin.register(Supportstaff)
class SupportstaffAdmin(admin.ModelAdmin):
    list_display=Supportstaff.Display_Supportstaff