from django.shortcuts import render
from django.http import HttpResponse
from .forms import CourseAddForm,BatchAddForm

# Create your views here.

# add course

def add_course(request):
    context = {}
    if request.method == "GET":

        form = CourseAddForm()
        context['form'] = form
        return render(request,'courseadd.html',context)
    elif request.method == "POST":
        form = CourseAddForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            c_name = form.cleaned_data["c_name"]
            fees = form.cleaned_data["fees"]

        # c_name = request.POST["coursename"]
            print(c_name,fees)
        return render(request,'courseadd.html',{'form':form})



def add_batch(request):
    context={}
    if request.method == "GET":
        form = BatchAddForm()
        context["form"] = form
        return render(request,'addbatch.html',context)

    elif request.method == "POST":
       form = BatchAddForm(request.POST)
       if form.is_valid():
           print(form.cleaned_data)
           c_name = form.cleaned_data['c_name']
           b_name = form.cleaned_data['b_name']
           b_code = form.cleaned_data['b_code']
           print(c_name,b_name,b_code)
    return render(request, 'addbatch.html',{'form':form})

def review_batch(request):
    return HttpResponse('<h1>Review Batch</h1>')
