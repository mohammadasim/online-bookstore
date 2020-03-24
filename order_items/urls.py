from django.urls import path

from .views import OrderProductsCreateView

urlpatterns = [
    path('create/', OrderProductsCreateView.as_view(), name='order_product_create'),
]
