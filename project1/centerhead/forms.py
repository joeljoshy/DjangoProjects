from django import forms

class CourseAddForm(forms.Form):
    c_name = forms.CharField()
    fees = forms.IntegerField()

class BatchAddForm(forms.Form):
    b_name = forms.CharField(label="Batch Name")
    c_name = forms.CharField(label="Course Name")
    b_code = forms.CharField(label="Batch Code")