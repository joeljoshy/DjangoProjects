from django.shortcuts import render,redirect
from .forms import AddBookForm,RegistrationForm,UpdateBookForm,CreateModelForm,SearchForm
from .models import AddBooks

# Create your views here.
def add_book(request):
    context = {}
    if request.method == "GET":
        form = CreateModelForm()
        context['form'] = form
        return render(request,'addbook.html',context)
    elif request.method == "POST":
        form = CreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # b_name = form.cleaned_data['b_name']
            # author = form.cleaned_data["author"]
            # cat = form.cleaned_data["cat"]
            # price = form.cleaned_data["price"]
            # no_copy = form.cleaned_data["no_copy"]
            # print("Book Name : ", b_name, "\nAuthor : ", author, "\nCategory : ", cat, "\nPrice : ", price,"\nNo: of copies : ", no_copy)
            # # saving to DB using ORM query
            # books = AddBooks(book_name=b_name,author=author,category=cat,price=price,copies=no_copy)
            # books.save()
            # return render(request, 'index.html')
            return redirect("index")
        else:
            return render(request, 'addbook.html', {'form': form})





def get_books(request):
    context = {}
    form = SearchForm()
    context['form'] = form
    books = AddBooks.objects.all()
    context['books'] = books
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["book_name"]
            books = AddBooks.objects.filter(book_name__contains=book_name)
            context['books'] = books
            return render(request, "book_list.html", context)
        else:
            context['form'] = form
            return render(request, "book_list.html", context)

    return render(request,"book_list.html",context)


def get_book(id):
    return AddBooks.objects.get(id=id)


def book_details(request,id):
    book = get_book(id)
    context = {}
    context['book'] = book
    return render(request,'view_book.html',context)


def delete(request ,id):
    book = get_book(id)
    book.delete()
    return redirect('booklist')


def update(request,id):
    book = get_book(id)
    form = CreateModelForm(instance=book)
    # form = UpdateBookForm(initial={
    #     'b_name':book.book_name,
    #     'author':book.author,
    #     'cat':book.category,
    #     'price':book.price,
    #     'no_copy':book.copies
    # })

    context={}
    context['form'] = form
    if request.method == "POST":
        book=get_book(id)
        form = CreateModelForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
        # form = UpdateBookForm(request.POST)
        # if form.is_valid():
        #     book.book_name=form.cleaned_data['b_name']
        #     book.author = form.cleaned_data['author']
        #     book.category = form.cleaned_data['cat']
        #     book.price = form.cleaned_data['price']
        #     book.copies = form.cleaned_data['no_copy']
        #     book.save()
            return redirect('booklist')
        else:
            form=CreateModelForm(request.POST)
            context['form'] = form
            print(form.errors)
            return render(request, 'edit_book.html', context)


    return render(request,'edit_book.html',context)


def create_account(request):
    form = RegistrationForm()
    context = {'form': form}
    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('account created')
            return render(request, 'registration.html', context)
        else:
            context={'form':form}
            return render(request, 'registration.html', context)
    return render(request, 'registration.html', context)