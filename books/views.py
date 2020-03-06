from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(ListView):
    """ A view class showing a list of books in the book store"""
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    """ A view class showing details of a single book """
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
