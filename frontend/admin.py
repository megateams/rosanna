from django.contrib import admin
from .models import Login, Admin_Model, Role_Model, Supportstaff, Student , Subjects , Schoolclasses , Teachers  , Marks

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
    
##################################
@admin.register(Student)
class MyClass(admin.ModelAdmin):
    list_display = Student.Display_Fields

@admin.register(Subjects)
class Displaysubject(admin.ModelAdmin):
    list_display = Subjects.Display_Subjects

@admin.register(Schoolclasses)
class Displayclasses(admin.ModelAdmin):
    list_display = Schoolclasses.Display_schoolclasses
    
@admin.register(Teachers)
class Displayteachers(admin.ModelAdmin):
    list_display = Teachers.Display_Teachers
    
@admin.register(Marks)
class Displayprimaryonemarks(admin.ModelAdmin):
    list_display = Marks.displaymarks