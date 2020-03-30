from django import forms
from django.forms import ModelForm

from .models import OrderItem


class OrderItemForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        """
        product/book object is passed to the form in kwargs in the view
        """
        self.book = kwargs.pop('book', None)
        super(OrderItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = OrderItem
        fields = [
            'quantity'
        ]

    def clean_quantity(self):
        """
        Method to check if the quantity ordered by customer
        is not more than quantity of we have in the stock
        """
        if self.initial:
            # For update we minus the initial quantity as that quantity
            # has already been subtracted from the book quantity
            quantity_ordered = self.cleaned_data.get('quantity') - self.initial.get('quantity')
            if quantity_ordered > self.book.quantity:
                if self.book.quantity <= 0:
                    raise forms.ValidationError('Sorry this item is out of stock now')
                else:
                    raise forms.ValidationError('There are only {} books in stock'.
                                                format(self.book.quantity))
            else:
                return self.cleaned_data.get('quantity')
        else:
            quantity_ordered = self.cleaned_data.get('quantity')
            if quantity_ordered > self.book.quantity:
                raise forms.ValidationError('Quantity ordered {} is more than what is in stock. '
                                            'The maximum quantity you can order is {}'.
                                            format(quantity_ordered, self.book.quantity))
            else:
                return quantity_ordered
