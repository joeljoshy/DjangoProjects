from django.shortcuts import render, redirect
from .forms import AddEmployeeForm
from .models import AddEmployee

# Create your views here.


def add_employee(request):
    context = {}
    if request.method == "GET":
        form = AddEmployeeForm()
        context['form'] = form
        return render(request, 'AddEmployee.html', context)
    elif request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            emp_name = form.cleaned_data['emp_name']
            desig = form.cleaned_data['desig']
            salary = form.cleaned_data['salary']
            exp = form.cleaned_data['exp']
            email = form.cleaned_data['email']

            emp = AddEmployee(emp_name=emp_name, desig=desig, salary=salary, exp=exp, email=email)
            emp.save()

            return redirect("index")
        else:
            return render(request, 'AddEmployee.html', {'form': form})