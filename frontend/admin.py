from django.contrib import admin

from .models import Students , Subjects , Schoolclasses , Teachers  , Marks

# Register your models here.

@admin.register(Students)
class MyClass(admin.ModelAdmin):
    list_display = Students.Display_Fields

@admin.register(Subjects)
class Displaysubject(admin.ModelAdmin):
    list_display = Subjects.Display_Subjects

@admin.register(Schoolclasses)
class Displayclasses(admin.ModelAdmin):
    list_display = Schoolclasses.Display_schoolclasses
    
@admin.register(Teachers)
class Displayteachers(admin.ModelAdmin):
    list_display = Teachers.Display_Teachers
    # list_display = Teachers.classrelationship

# @admin.register(primaryonestds)
# class Displayp1stds(admin.ModelAdmin):
#     list_display = primaryonestds.displayprimaryone
    
@admin.register(Marks)
class Displayprimaryonemarks(admin.ModelAdmin):
    list_display = Marks.displaymarks
    

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
