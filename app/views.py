from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import EmployeeForm, ManagerForm
from .models import Employee, Manager


def list_managers(request):
    managers = Manager.objects.all()
    return render(request, 'managers.html', {'managers': managers})


def create_manager(request):
    form = ManagerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/coordenador/')

    return render(request, 'create_manager.html', {'form': form})


def edit_manager(request, pk):
    manager = get_object_or_404(Manager, id=pk)
    form = ManagerForm(request.POST or None, instance=manager)

    if form.is_valid():
        form.save()
        return redirect('/coordenador/')

    return render(request, 'create_manager.html', {'form': form})


def delete_manager(request, pk):
    manager = get_object_or_404(Manager, id=pk)

    if request.method == 'POST':
        manager.delete()
        return redirect('/coordenador/')

    return render(request, 'delete_manager.html')

def list_employees(request):
    employees = Employee.objects.all()

    return render(request, 'employees.html', {'employees': employees})

def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/funcionario/')

    return render(request, 'create_employee.html', {'form': form})


def edit_employee(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('/funcionario/')

    return render(request, 'create_employee.html', {'form': form})


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('/funcionario/')

    return render(request, 'delete_employee.html')

def get_managers(request):
    city = request.GET.get('city', None)
    
    if city:
        managers = list(Manager.objects.filter(city=city).values('id', 'name'))
    else:
        managers = list(Manager.objects.all().values('id', 'name'))

    response_data = {
        'managers': managers
    }

    return JsonResponse(response_data)


def hello_world(request):
    return render(request, 'test.html')
