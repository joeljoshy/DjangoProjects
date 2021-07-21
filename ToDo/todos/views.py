from django.shortcuts import render
from .forms import TodoForm

# Create your views here.
def todo(request):
    context = {}
    if request.method == "GET":
        form = TodoForm()
        context['form'] = form
        return render(request,'todo.html',context)
    elif request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            task_name = form.cleaned_data['task_name']
            status = form.cleaned_data['status']
            user = form.cleaned_data['user']
            print("Task Name : ",task_name,"\nStatus : ",status,"\nUser : ",user)
            return render(request,'todo.html')
        else:
            return render(request, 'todo.html', {'form':form})
