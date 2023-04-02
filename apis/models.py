from django.db import models

# Employee model


class Employee(models.Model):
    employee_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    # will convert unique EMP-ID auto increment
    def save(self, *args, **kwargs):
        if not self.employee_code:
            employees_count = Employee.objects.count()
            self.employee_code = f"EMP-{employees_count+1:03d}"
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Vendor model


class Vendor(models.Model):
    vendor_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    # will convert unique VEN-ID auto increment
    def save(self, *args, **kwargs):
        if not self.vendor_code:
            vendor_count = Vendor.objects.count()
            self.vendor_code = f"VEN-{vendor_count+1:03d}"
        super(Vendor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Expense model


class Expense(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expense_comment = models.CharField(max_length=200)
    expense_done_on = models.DateField()
    expense_amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.employee.name} - {self.vendor.name} - {self.expense_amount} - {self.expense_done_on.strftime('%d-%b-%Y')}"
