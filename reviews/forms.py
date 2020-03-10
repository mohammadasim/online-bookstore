from django.forms import ModelForm

from .models import Review


class ReviewForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Review
        fields = [
            'title', 'review', 'type', 'book'
        ]
