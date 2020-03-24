from django.forms import ModelForm

from .models import CustomerOrderProduct


class OrderProductForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        """
        product/book object is passed to the form in kwargs in the view
        """
        self.book = kwargs.pop('book', None)
        super(OrderProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomerOrderProduct
        fields = [
            'quantity'
        ]
