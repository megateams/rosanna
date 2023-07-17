from django.contrib import admin
from .models import Registration , Subjects , Schoolclasses , Teachers

# Register your models here.

@admin.register(Registration)
class MyClass(admin.ModelAdmin):
    list_display = Registration.Display_Fields

@admin.register(Subjects)
class Displaysubject(admin.ModelAdmin):
    list_display = Subjects.Display_Subjects

@admin.register(Schoolclasses)
class Displayclasses(admin.ModelAdmin):
    list_display = Schoolclasses.Display_schoolclasses
    
@admin.register(Teachers)
class Displayteachers(admin.ModelAdmin):
    list_display = Teachers.Display_Teachers


