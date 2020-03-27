from django.urls import path

from .views import OrderDetailView

# register a namespace
app_name = 'orders'

urlpatterns = [
    path('<slug>', OrderDetailView.as_view(), name='order_detail'),
]
