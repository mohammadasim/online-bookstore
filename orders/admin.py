from django.contrib import admin

from .models import CustomerOrder


class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'customer_id',
        'payment_id',
        'order_date',
        'order_status',
        'order_price'
    )
    list_filter = ('order_date', 'customer_id', 'order_status', 'payment_id', 'order_price')
    readonly_fields = ('customer_id', 'payment_id')


admin.site.register(CustomerOrder, CustomerOrderAdmin)
