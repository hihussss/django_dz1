from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    book = Book.objects.all()
    context = {
        'books': book
    }
    return render(request, template, context)

def pagi(request, pub_date):
    template = 'books/pagi.html'
    book_page = int(request.GET.get('page',1))
    data_all = Book.objects.values('pub_date')
    books_obj = Book.objects.get(pub_date=pub_date)
    paginator = Paginator(data_all, 1)
    page = paginator.get_page(book_page) 
    context = {
        
        'book': books_obj,
        'page': page
    }
    return render(request, template, context)