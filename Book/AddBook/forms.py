from django import forms
from .models import AddBooks

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

class RegistrationForm(forms.Form):
    f_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    l_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    u_name = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    c_pwd = forms.CharField(label="Confirm-Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))


    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data['pwd']
        c_pwd = cleaned_data['c_pwd']

        try:
            if pwd != c_pwd:
                msg = "Password mismatch!!"
                self.add_error('c_pwd',msg)
        except:
            msg = "Password mismatch!!"
            self.add_error('c_pwd', msg)






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

