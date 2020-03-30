from django.urls import path

from .views import order_item_create_view, OrderItemDelete, OrderItemUpdate

# register a namespace
app_name = 'order_items'

urlpatterns = [
    path('create/<uuid:uuid>', order_item_create_view, name='order_item_create'),
    path('delete/<slug>', OrderItemDelete.as_view(), name='order_item_delete'),
    path('update/<slug>', OrderItemUpdate.as_view(), name='order_item_update'),
]
