from django.contrib import admin

from .models import Book
from .tasks import upload_cover_to_s3


class BookAdmin(admin.ModelAdmin):
    """ A class configuring Books setup in django admin """
    list_display = ("title", "author", "price")

    # Prepopulate the slug field using title
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        """ Method overridden to invoke celery task to upload cover to s3"""
        book_title = form.cleaned_data.get('title')
        book_title_slug = form.cleaned_data.get('slug')
        super().save_model(request, obj, form, change)
        book = Book.objects.get(title=book_title)
        upload_cover_to_s3.delay(book.cover.path, book_title_slug)


admin.site.register(Book, BookAdmin)
