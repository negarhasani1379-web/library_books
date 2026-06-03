from django.shortcuts import render
from .models import Book

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
    return render(request)

