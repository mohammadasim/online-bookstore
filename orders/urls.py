from django.urls import path

from .views import OrderDetailView, OrderListView, OrderDeleteView

# register a namespace
app_name = 'orders'

urlpatterns = [
    path('show', OrderListView.as_view(), name='show_orders'),
    path('delete/<slug>', OrderDeleteView.as_view(), name='order_delete'),
    path('<slug>', OrderDetailView.as_view(), name='order_detail'),
]
