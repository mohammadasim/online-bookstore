import os

from django.contrib import admin

from .models import Book
from .tasks import delete_object_from_s3

s3_bucket_name = os.environ.get('AWS_S3_BUCKET_NAME')


def delete_book_and_cover(modeladmin, request, queryset):
    """
    django default delete method doesn't delete book cover in s3.
    This custom action deletes both the book and the book cover.
    Deleting cover from s3 through is done using a celery task
    """

    for obj in queryset:
        if obj.cover:
            delete_object_from_s3.delay(s3_bucket_name,
                                        str(obj.cover))
        obj.delete()


class BookAdmin(admin.ModelAdmin):
    """ A class configuring Books setup in django admin """
    list_display = ("title", "author", "price")

    # Prepopulate the slug field using title
    prepopulated_fields = {'slug': ('title',)}
    # Adding custom action to modeladmin
    actions = [delete_book_and_cover]

    def save_form(self, request, form, change):
        """
        Overriding the method to delete the old book cover
        when book cover is updated
        """
        if change:
            old_book_cover = (Book.objects.get(title=form.cleaned_data.get('title'))).cover
            print(str(old_book_cover))
            new_book_cover = str(form.cleaned_data.get('cover'))
            if old_book_cover and old_book_cover != new_book_cover:
                delete_object_from_s3.delay(s3_bucket_name,
                                            str(old_book_cover))
                return form.save(commit=False)
            else:
                return form.save(commit=False)
        return form.save(commit=False)


admin.site.register(Book, BookAdmin)
