from django.shortcuts import render
from .models import Employee


def home(request):
    return render(request,'create.html')


def insert(request):
    emp=Employee()
    name=request.GET.get('name')
    emp_id=request.GET.get('emp_id')
    email=request.GET.get('email')
    phone=request.GET.get('phone')
    address=request.GET.get('address'),
    dob=request.GET.get('dob')
    dept=request.GET.get('department')
    emp.name=name
    emp.emp_id=emp_id
    emp.email=email
    emp.phone=phone
    emp.address=address
    emp.dob=dob
    emp.department=dept
    emp.save()
    return render(request,'create.html')

def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})


def update(request):
    emp_id=request.GET.get('emp_id')
    emp=Employee.objects.get(emp_id=emp_id)
    return render(request,'update.html',{'emp':emp})