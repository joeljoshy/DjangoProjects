from django.urls import path
from django.shortcuts import render
from .views import add_employee

urlpatterns = [
    path('AddEmployee',add_employee,name="addemployee"),
    path("",lambda request:render(request,"index.html"),name='index')
]