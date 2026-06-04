from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def home(request):
    return render(request,'books/home.html')


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'books/book_list.html', context)

def book_detail(request,id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request,'books/book_detail.html', context)

def book_create_update(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        context = {'form':form}    
        return render(request,'books/book_form.html', context)

