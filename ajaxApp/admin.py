from django.contrib import admin
from .models import Employee, Office
# Register your models here.

class EmployeeInline(admin.TabularInline):
    model = Employee


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    list_display_links = ('name', 'location',)
    inlines = [ EmployeeInline ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'office')
    list_display_links = ('first_name', 'last_name',
                          'email', 'gender', 'office')
    
