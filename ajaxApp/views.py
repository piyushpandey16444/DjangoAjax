from django.shortcuts import render
from .models import Employee, Office
from .forms import EmployeeForm, OfficeForm

# Create your views here.

def home(request):
    office_form = OfficeForm()
    employee_form = EmployeeForm()
    context = {
        'oform': office_form,
        'eform': employee_form,
    }
    return render(request, 'ajaxApp/index.html', context=context)

