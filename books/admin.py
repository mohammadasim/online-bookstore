import os

from django.contrib import admin

from .helpers import create_boto3_client
from .models import Book


def delete_book_and_cover(modeladmin, request, queryset):
    """
    django default delete method doesn't delete book cover in s3.
    This custom action deletes both the book and the book cover.
    """
    client = create_boto3_client('s3')
    s3_bucket_name = os.environ.get('AWS_S3_BUCKET_NAME')
    for obj in queryset:
        client.delete_object(
            Bucket=s3_bucket_name,
            Key=str(obj.cover))
        obj.delete()


class BookAdmin(admin.ModelAdmin):
    """ A class configuring Books setup in django admin """
    list_display = ("title", "author", "price")

    # Prepopulate the slug field using title
    prepopulated_fields = {'slug': ('title',)}
    # Adding custom action to modeladmin
    actions = [delete_book_and_cover]


admin.site.register(Book, BookAdmin)
