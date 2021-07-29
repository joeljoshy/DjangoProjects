from django.shortcuts import render, redirect
from .forms import AddEmployeeForm,UpdateEmployeeForm,SearchForm,CreateModelForm,RegistrationForm
from .models import AddEmployee

# Create your views here.


def add_employee(request):
    context = {}
    if request.method == "GET":
        form = CreateModelForm()
        context['form'] = form
        return render(request, 'AddEmployee.html', context)
    elif request.method == "POST":
        form = CreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # emp_name = form.cleaned_data['emp_name']
            # desig = form.cleaned_data['desig']
            # salary = form.cleaned_data['salary']
            # exp = form.cleaned_data['exp']
            # email = form.cleaned_data['email']
            #
            # emp = AddEmployee(emp_name=emp_name, desig=desig, salary=salary, exp=exp, email=email)
            # emp.save()

            return redirect("index")
        else:
            return render(request, 'AddEmployee.html', {'form': form})


def get_employee(request):
    context = {}
    form = SearchForm()
    context['form'] = form
    emps = AddEmployee.objects.all()
    context['emps'] = emps
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            emps = AddEmployee.objects.filter(emp_name__contains=emp_name)
            context['emps'] = emps
            return render(request, "employee_list.html", context)
        else:
            context['form'] = form
            return render(request, "employee_list.html", context)

    return render(request,"employee_list.html",context)

def get_emp(id):
    return AddEmployee.objects.get(id=id)

def emp_details(request,id):
    emp = get_emp(id)
    context = {}
    context['emp'] = emp
    return render(request,'view_employee.html',context)

def delete(request,id):
    emp = get_emp(id)
    emp.delete()
    return redirect('emplist')

def update(request,id):
    emp = get_emp(id)
    form = CreateModelForm(instance=emp)
    # form = UpdateEmployeeForm(initial={
    #     'emp_name':emp.emp_name,
    #     'desig':emp.desig,
    #     'salary':emp.salary,
    #     'exp':emp.exp,
    #     'email':emp.email
    # })
    context={}
    context['form']=form
    if request.method == "POST":
        emp = get_emp(id)
        form = CreateModelForm(instance=emp,data=request.POST)
        if form.is_valid():
            form.save()
            # emp.emp_name=form.cleaned_data['emp_name']
            # emp.desig=form.cleaned_data['desig']
            # emp.salary=form.cleaned_data['salary']
            # emp.exp = form.cleaned_data['exp']
            # emp.email = form.cleaned_data['email']
            # emp.save()
            return redirect('emplist')
        else:
            form = CreateModelForm(request.POST)
            context['form'] = form
            print(form.errors)
            return render(request,'edit_employee.html',context)

    return render(request,'edit_employee.html',context)

def create_account(request):
    form = RegistrationForm()
    context = {'form':form}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return render(request,'registration.html',context)
        else:
            context = {'form':form}
            return render(request,'registration.html',context)
    return render(request,'registration.html',context)