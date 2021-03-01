from django import forms
from .models import Office, Employee


class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
