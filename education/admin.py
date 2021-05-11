from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Departments)
admin.site.register(Faculty)
admin.site.register(Speciality)
admin.site.register(EducationGroup)
admin.site.register(Subjects)
admin.site.register(Topic)
admin.site.register(Tag)


#admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_filter = ('department_s',)

    fieldsets = (
        ('Personal information', {
            'fields': ('tcode', 'last_name', 'first_name', 'middle_name', 'gender', 'email')
        }),
        ('Department', {
            'fields': ('department_s', 'employee_post', 'academic_degree')
        }),
        ('Department', {
            'fields': ('t_tag',)
        }),
    )

admin.site.register(Teachers, TeachersAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'edu_group')

@admin.register(Paperwork)
class PaperworkAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'deadline')