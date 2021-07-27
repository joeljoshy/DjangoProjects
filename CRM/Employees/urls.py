from django.urls import path
from django.shortcuts import render
from .views import add_employee,get_employee,emp_details,delete,update

urlpatterns = [
    path('AddEmployee',add_employee,name="addemployee"),
    path("",lambda request:render(request,"index.html"),name='index'),
    path('employees',get_employee,name='emplist'),
    path('employees/<int:id>',emp_details,name='details'),
    path('employees/remove/<int:id>',delete,name='remove'),
    path('employees/change/<int:id>',update,name='update')
]