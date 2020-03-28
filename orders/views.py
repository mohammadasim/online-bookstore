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

    # def get(self, request, *args, **kwargs):
    #     order_placed = get_object_or_404(CustomerOrder,
    #                                      order_id=kwargs['slug'],
    #                                      customer_id=request.user)
    #     print(type(order_placed))
    #     context = {
    #         'object': order_placed
    #     }
    #     return render(request, self.template_name, context=context)
