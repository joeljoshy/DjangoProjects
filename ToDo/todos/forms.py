from django import forms


class TodoForm(forms.Form):
    task_name = forms.CharField(label="Task Name", widget=forms.Textarea(attrs={'class': "form-control"}))
    status = forms.CharField(label="Status", widget=forms.TextInput(attrs={'class': "form-control"}))
    user = forms.CharField(label="User", widget=forms.TextInput(attrs={'class': "form-control"}))
