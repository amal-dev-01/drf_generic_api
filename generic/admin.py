from django.contrib import admin


from generic.models import Student

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city') 

admin.site.register(Student, StudentsAdmin)