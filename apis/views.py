from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from apis.models import Employee, Vendor, Expense
from rest_framework.decorators import api_view
from rest_framework import status
from apis.serializers import EmployeeSerializer, VendorSerializer, ExpenseSerializer


# EMPLOYEE

# get_employee_api
@api_view(['GET', 'POST'])
def get_employee_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            emp = Employee.objects.get(employee_code=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

# add_employee_api


@api_view(['POST'])
def add_employee_api(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# VENDOR

# get_vendor_api


@api_view(['GET', 'POST'])
def get_vendor_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            ven = Vendor.objects.get(vendor_code=id)
            serializer = VendorSerializer(ven)
            return Response(serializer.data)

        ven = Vendor.objects.all()
        serializer = VendorSerializer(ven, many=True)
        return Response(serializer.data)

# add_vendor_api


@api_view(['POST'])
def add_vendor_api(request):
    if request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Vendor Created'},  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  EXPENSE

@api_view(['POST'])
def add_expense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'expense created.'})
    else:
        return Response(serializer.errors, status=400)

# get_expense_for_vendor


@api_view(['GET'])
def get_expense_for_employee(request, pk=None):
    employee_code = request.query_params.get('employee_code', '')
    employee = get_object_or_404(Employee, vendor_code=pk)
    expenses = Expense.objects.filter(vendor=employee)
    serializer = ExpenseSerializer(expenses, many=True)
    response_data = {
        'name': employee.name,
        'expenses': serializer.data
    }
    return Response(response_data)

# get_expense_for_vendor


@api_view(['GET'])
def get_expense_for_vendor(request, pk=None):
    vendor_code = request.query_params.get('vendor_code', '')
    vendor = get_object_or_404(Vendor, vendor_code=pk)
    expenses = Expense.objects.filter(vendor=vendor)
    serializer = ExpenseSerializer(expenses, many=True)
    response_data = {
        'name': vendor.name,
        'expenses': serializer.data
    }
    return Response(response_data)
