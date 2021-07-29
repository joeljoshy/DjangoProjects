from django.urls import path
from django.shortcuts import render
from .views import add_book,get_books,book_details,delete,update,create_account

urlpatterns = [
    path('Addbook',add_book,name="addbook"),
    # path('Register',register,name="register"),
    path("",lambda request:render(request,"index.html"),name="index"),
    path('books/account',create_account,name='account'),
    path('books',get_books,name="booklist"),
    path('books/<int:id>',book_details,name='details'),
    path('books/remove/<int:id>',delete,name='remove'),
    path('books/change/<int:id>',update,name='update')

    ]