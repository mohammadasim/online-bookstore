from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    """ A class configuring Books setup in django admin """
    list_display = ("title", "author", "price")


admin.site.register(Book, BookAdmin)
