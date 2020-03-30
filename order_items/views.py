from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from books.models import Book
from orders.models import CustomerOrder
from .forms import OrderItemForm
from .models import OrderItem


@login_required(login_url=reverse_lazy('account_login'))
def order_item_create_view(request, uuid):
    """
    A view to create an order_item for a book and add it
    either an existing pending order or create a new order
    """
    # First we have to retrieve the book
    book = get_object_or_404(Book, id=uuid)
    if request.method == 'GET':
        form = OrderItemForm(book=book)
        context = {
            'form': form,
            'book': book
        }
        return render(request, 'order_items/order_item_create.html', context=context)
    if request.method == 'POST':
        # load data from the request
        form = OrderItemForm(request.POST, book=book)
        # check if the form is valid
        if form.is_valid():
            order_item = form.save(commit=False)
            # check if there is a pending order for customer
            order = CustomerOrder.objects.filter(customer_id=request.user, order_status='PND')
            if order.exists():
                # if there is a pending order for the customer, check if the book ordered is in the order
                book_already_ordered = OrderItem.objects.filter(book=book, order_id__in=order)
                if book_already_ordered.exists():
                    # if it exists add the quantity ordered to the existing quantity
                    book_already_ordered.first().quantity += order_item.quantity
                    book_already_ordered.first().save()
                    return redirect('orders:order_detail', slug=order.first().order_id)
                else:
                    # Create a new order_item for the book
                    new_order_item = OrderItem(quantity=order_item.quantity,
                                               book=book,
                                               order_id=order.first())
                    new_order_item.save()
                    order.first().save()

                    return redirect('orders:order_detail', slug=order.first().order_id)
            else:
                # If there isn't any pending order for the customer
                new_order = CustomerOrder(customer_id=request.user)
                # Create new order_item for the book
                new_order_item = OrderItem(quantity=order_item.quantity,
                                           order_id=new_order,
                                           book=book
                                           )
                new_order.save()
                new_order_item.save()
                return redirect('orders:order_detail', slug=new_order.order_id)
        context = {
            'form': form,
            'book': book
        }
        return render(request, 'order_items/order_item_create.html', context=context)


class OrderItemDelete(LoginRequiredMixin, DeleteView):
    """
    View to delete an Order item from an order
    """
    model = OrderItem
    success_url = reverse_lazy('orders:show_orders')
    template_name = 'order_items/order_item_delete.html'
    login_url = reverse_lazy('account_login')
    slug_field = 'id'


class OrderItemUpdate(LoginRequiredMixin, UpdateView):
    """
    View to update an Order item
    """
    model = OrderItem
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('orders:show_orders')
    template_name = 'order_items/order_item_update.html'
    slug_field = 'id'
    form_class = OrderItemForm

    def get_form_kwargs(self):
        """
        OrderItemForm expects a book object as kwargs
        This method retrieves the associated book object
        and pass it to the form
        """
        kwargs = super(OrderItemUpdate, self).get_form_kwargs()
        book = self.get_object().book
        kwargs['book'] = book
        return kwargs
