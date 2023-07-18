from django.contrib import admin
from .models import Students , Subjects , Schoolclasses , Teachers  , marks

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
    
@admin.register(marks)
class Displayprimaryonemarks(admin.ModelAdmin):
    list_display = marks.displaymarks
    



