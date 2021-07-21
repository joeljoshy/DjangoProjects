from django.shortcuts import render
from .forms import AddBookForm,RegistrationForm


# Create your views here.
def add_book(request):
    context = {}
    if request.method == "GET":
        form = AddBookForm()
        context['form'] = form
        return render(request,'addbook.html',context)
    elif request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            b_name = form.cleaned_data['b_name']
            author = form.cleaned_data["author"]
            cat = form.cleaned_data["cat"]
            price = form.cleaned_data["price"]
            no_copy = form.cleaned_data["no_copy"]
            print("Book Name : ", b_name, "\nAuthor : ", author, "\nCategory : ", cat, "\nPrice : ", price,"\nNo: of copies : ", no_copy)
            return render(request, 'addbook.html')

        else:
            return render(request, 'addbook.html', {'form': form})


def register(request):
    context = {}
    if request.method == "GET":
        form = RegistrationForm()
        context['form'] = form
        return render(request,'registration.html',context)
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            email = form.cleaned_data['email']
            u_name = form.cleaned_data['u_name']
            print("First Name : ", f_name, "\nLast Name : ", l_name, "\nEmail : ", email, "\nUsername : ", u_name)



        return render(request, 'registration.html', {'form': form})


