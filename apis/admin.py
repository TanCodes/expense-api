from django.contrib import admin
from .models import Employee, Vendor, Expense
# Register your models here.


@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['employee_code', 'name']


@admin.register(Vendor)
class VenAdmin(admin.ModelAdmin):
    list_display = ['vendor_code', 'name']


@admin.register(Expense)
class ExpAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'employee', 'expense_comment',
                    'expense_done_on', 'expense_amount']
