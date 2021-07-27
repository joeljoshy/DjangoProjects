from django import forms
from .models import AddEmployee


class AddEmployeeForm(forms.Form):

    emp_name = forms.CharField(label="Employee Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    desig = forms.CharField(label="Designation", widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.FloatField(label="Salary", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exp = forms.IntegerField(label="Experience", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        salary = cleaned_data['salary']
        exp = cleaned_data['exp']

        emp = AddEmployee.objects.filter(email__iexact=email)
        if emp:
            msg = "Employee already exists!!"
            self.add_error("email", msg)

        try:
            if salary <= 0:
                msg = "Invalid Salary"
                self.add_error("salary", msg)
        except:
            msg = "Invalid Salary"
            self.add_error("salary", msg)

        try:
            if exp < 0:
                msg = "Invalid Experience!!"
                self.add_error("exp", msg)
        except:
            msg = "Invalid Experience!!"
            self.add_error("exp", msg)

class UpdateEmployeeForm(forms.Form):

    emp_name = forms.CharField(label="Employee Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    desig = forms.CharField(label="Designation", widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.FloatField(label="Salary", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exp = forms.IntegerField(label="Experience", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        salary = cleaned_data['salary']
        exp = cleaned_data['exp']

        emp = AddEmployee.objects.filter(email__iexact=email)


        try:
            if salary <= 0:
                msg = "Invalid Salary"
                self.add_error("salary", msg)
        except:
            msg = "Invalid Salary"
            self.add_error("salary", msg)

        try:
            if exp < 0:
                msg = "Invalid Experience!!"
                self.add_error("exp", msg)
        except:
            msg = "Invalid Experience!!"
            self.add_error("exp", msg)
