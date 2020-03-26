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
        quantity_ordered = self.cleaned_data.get('quantity')
        if quantity_ordered > self.book.quantity:
            raise forms.ValidationError('Quantity ordered {} is more than what is in stock'
                                        'The maximum quantity you can order is {}'.
                                        format(quantity_ordered, self.book.quantity))
        else:
            return quantity_ordered
