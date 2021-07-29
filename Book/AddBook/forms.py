from django import forms
from .models import AddBooks
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddBookForm(forms.Form):
    b_name = forms.CharField(label="Book Name",widget=forms.TextInput(attrs={'class':"form-control"}))
    author = forms.CharField(label="Author",widget=forms.TextInput(attrs={'class':"form-control"}))
    cat = forms.CharField(label="Category",widget=forms.TextInput(attrs={'class':"form-control"}))
    price = forms.FloatField(label="Price",widget=forms.NumberInput(attrs={'class':"form-control"}))
    no_copy = forms.CharField(label="No: of Copies",widget=forms.NumberInput(attrs={'class':"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        book_name=cleaned_data['b_name']
        price = cleaned_data['price']
        no_copy = cleaned_data['no_copy']
        books = AddBooks.objects.filter(book_name__iexact=book_name)
        if books:
            msg = "Book Already exists!!"
            self.add_error("b_name",msg)
        try:
            price = int(price)
            if price < 0:
                msg = "Invalid Price!!"
                self.add_error("price", msg)
        except:
             msg = "Invalid Price!!"
             self.add_error("price", msg)

        try:
            no_copy = int(no_copy)
            if no_copy < 0:
                msg = "Invalid Copies!!"
                self.add_error("no_copy", msg)
        except:
            msg = "Invalid Copies!!"
            self.add_error("no_copy", msg)

class UpdateBookForm(forms.Form):
    b_name = forms.CharField(label="Book Name",widget=forms.TextInput(attrs={'class':"form-control"}))
    author = forms.CharField(label="Author",widget=forms.TextInput(attrs={'class':"form-control"}))
    cat = forms.CharField(label="Category",widget=forms.TextInput(attrs={'class':"form-control"}))
    price = forms.FloatField(label="Price",widget=forms.NumberInput(attrs={'class':"form-control"}))
    no_copy = forms.CharField(label="No: of Copies",widget=forms.NumberInput(attrs={'class':"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        book_name=cleaned_data['b_name']
        price = cleaned_data['price']
        no_copy = cleaned_data['no_copy']
        books = AddBooks.objects.filter(book_name__iexact=book_name)

        try:
            price = int(price)
            if price < 0:
                msg = "Invalid Price!!"
                self.add_error("price", msg)
        except:
             msg = "Invalid Price!!"
             self.add_error("price", msg)

        try:
            no_copy = int(no_copy)
            if no_copy < 0:
                msg = "Invalid Copies!!"
                self.add_error("no_copy", msg)
        except:
            msg = "Invalid Copies!!"
            self.add_error("no_copy", msg)


class CreateModelForm(ModelForm):
    class Meta:
        model = AddBooks
        fields = "__all__"

        widgets = {
            "book_name": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "copies": forms.NumberInput(attrs={'class': 'form-control'})
        }

        def clean(self):
            cleaned_data = super().clean()
            # book_name = cleaned_data['b_name']
            price = cleaned_data['price']
            copies = cleaned_data['copy']
            # books = AddBooks.objects.filter(book_name__iexact=book_name)
            # if books:
            #     msg = "Book Already exists!!"
            #     self.add_error("b_name", msg)
            try:
                price = int(price)
                if price <= 0:
                    msg = "Invalid Price!!"
                    self.add_error("price", msg)
            except:
                msg = "Invalid Price!!"
                self.add_error("price", msg)

            try:
                no_copy = int(copies)
                if no_copy < 0:
                    msg = "Invalid Copies!!"
                    self.add_error("copies", msg)
            except:
                msg = "Invalid Copies!!"
                self.add_error("copies", msg)

class SearchForm(forms.Form):
    book_name = forms.CharField(max_length=20,widget=(forms.TextInput(attrs={'class':'form-control'})))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','password1','password2']

    widgets = {
        "first_name": forms.TextInput(attrs={'class': 'form-control'}),
        "username": forms.TextInput(attrs={'class': 'form-control'}),
        "password1": forms.TextInput(attrs={'class': 'form-control'}),
        "password2": forms.NumberInput(attrs={'class': 'form-control'})
    }