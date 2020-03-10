from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import ReviewForm
from .models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """ A view to create a new Review """
    template_name = 'reviews/review_create_form.html'
    form_class = ReviewForm
    success_url = '/'
    login_url = reverse_lazy('account_login')

    def form_valid(self, form):
        review = form.save(commit=False)
        try:
            review.author = self.request.user
        except ObjectDoesNotExist:
            pass
        review.save()
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """ A view to update an existing review """
    model = Review
    fields = [
        'title',
        'review',
        'type'
    ]
    template_name = 'reviews/review_update_form.html'
    success_url = reverse_lazy('book_list')
