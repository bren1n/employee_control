from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import ManagerForm
from .models import Manager


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


def hello_world(request):
    return render(request, 'test.html')
