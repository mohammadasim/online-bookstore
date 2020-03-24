from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import OrderProductForm


class OrderProductsCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create an order for a single product/book in an order
    """
    template_name = 'order_items/order_product_create_form.html'
    success_url = 'the_order_detail_url'
    login_url = reverse_lazy('account_login')
    form_class = OrderProductForm
