
from django.contrib import admin
from django.urls import path
from apis import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("get-employee/", views.get_employee_api),
    path("get-employee/employee-code=<int:pk>", views.get_employee_api),
    path("add-employee/", views.add_employee_api),

    path("get-vendor/", views.get_vendor_api),
    path("get-vendor/vendor-code=<int:pk>", views.get_vendor_api),
    path("add-vendor/", views.add_vendor_api),

    path('add-expense/', views.add_expense, name='create_expense'),
    path('get-expense-for-employee/employee-code=<int:pk>', views.get_expense_for_employee,
         name='get_expense_for_employee'),
    path('get-expense-for-vendor/vendor-code=<int:pk>', views.get_expense_for_vendor,
         name='get_expense_for_vendor'),
]
