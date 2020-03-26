from django.urls import path

from .views import order_item_create_view

# register a namespace
app_name = 'order_items'

urlpatterns = [
    path('create/<uuid:uuid>', order_item_create_view, name='order_product_create'),
]
