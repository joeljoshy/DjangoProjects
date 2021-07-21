from django.urls import path
from django.shortcuts import render
from .views import add_book,register

urlpatterns = [
    path('Addbook',add_book,name="addbook"),
    path('Register',register,name="register"),
    path("",lambda request:render(request,"index.html"),name="index")
    ]