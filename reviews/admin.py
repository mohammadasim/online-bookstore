from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'type',
                    'update_date',
                    'book',
                    'author')

    list_filter = ('book', 'author', 'update_date', 'type')

    readonly_fields = ('title', 'title', 'update_date', 'type', 'author', 'book', 'review')


admin.site.register(Review, ReviewAdmin)
