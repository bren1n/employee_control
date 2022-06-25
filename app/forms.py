from django import forms
from .models import City, Employee, Manager


class ManagerForm(forms.ModelForm):
    # city = forms.ModelChoiceField(queryset=City.objects.all())

    class Meta:
        model = Manager
        fields = ('name', 'phone', 'city')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }


class EmployeeForm(forms.ModelForm):
    # city = forms.ModelChoiceField(queryset=City.objects.all())

    class Meta:
        model = Employee
        fields = ('name', 'phone', 'city')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }
