from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from .models import CustomerOrder


class OrderDetailView(LoginRequiredMixin, DetailView):
    """
    View to show details of the order placed by a customer
    """
    model = CustomerOrder
    login_url = reverse_lazy('account_login')
    template_name = 'orders/customer_order_detail.html'
    slug_field = 'order_id'


class OrderListView(LoginRequiredMixin, ListView):
    """
    A view to list customer orders
    """
    model = CustomerOrder
    login_url = reverse_lazy('account_login')
    template_name = 'orders/customer_order_list.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        """
        Show only the logged in customer's orders
        """
        return CustomerOrder.objects.filter(customer_id=self.request.user)
