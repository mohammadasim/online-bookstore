from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .models import CustomerOrder


class OrderDetailView(LoginRequiredMixin, DetailView):
    """
    View to show details of the order placed by a customer
    """
    model = CustomerOrder
    login_url = reverse_lazy('account_login')
    template_name = 'orders/customer_order_detail.html'
    slug_field = 'order_id'

    def get_queryset(self):
        """
        Method to show only a pending customer order
        """
        return CustomerOrder.objects.get(order_id=self.kwargs['slug'])
