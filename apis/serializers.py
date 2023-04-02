from rest_framework import serializers
from apis.models import Employee, Vendor, Expense

# Employee serializers


class EmployeeSerializer(serializers.ModelSerializer):
    employee_code = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ("employee_code", "name")


# vendor serializers
class VendorSerializer(serializers.ModelSerializer):
    vendor_code = serializers.ReadOnlyField()

    class Meta:
        model = Vendor
        fields = ("vendor_code", "name")

# expense serializers


class ExpenseSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    vendor_name = serializers.SerializerMethodField()

    def get_employee_name(self, obj):
        return obj.get_employee_name()

    def get_vendor_name(self, obj):
        return obj.get_vendor_name()

    class Meta:
        model = Expense
        fields = "__all__"
