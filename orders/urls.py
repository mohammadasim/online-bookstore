from django.urls import path

from .views import OrderDetailView, OrderListView

# register a namespace
app_name = 'orders'

urlpatterns = [
    path('show', OrderListView.as_view(), name='show-orders'),
    path('<slug>', OrderDetailView.as_view(), name='order_detail'),
]
