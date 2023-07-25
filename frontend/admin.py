from django.contrib import admin
from .models import Student , Subjects , Schoolclasses , Teachers  , Marks

# Register your models here.

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
    # list_display = Teachers.classrelationship

# @admin.register(primaryonestds)
# class Displayp1stds(admin.ModelAdmin):
#     list_display = primaryonestds.displayprimaryone
    
@admin.register(Marks)
class Displayprimaryonemarks(admin.ModelAdmin):
    list_display = Marks.displaymarks
    



