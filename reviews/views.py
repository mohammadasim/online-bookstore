from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import ReviewForm
from .models import Review
from .tasks import print_greetings


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """ A view to create a new Review """
    template_name = 'reviews/review_create_form.html'
    form_class = ReviewForm
    success_url = '/'
    login_url = reverse_lazy('account_login')

    def form_valid(self, form):
        review = form.save(commit=False)
        book = form.cleaned_data.get('book')
        review_type = form.cleaned_data.get('type')
        try:
            review.author = self.request.user
        except ObjectDoesNotExist:
            pass
        review.save()
        print_greetings.delay(100, review_type)
        return super().form_valid(form)

    def get_form_kwargs(self):
        """
        This method returns a dictionary with the kwargs that will be passed
        to the __init__ of the ReviewForm. Our form expects a kwargs named
        'user'. We add user to the kwargs so that our form gets it.
        """
        kwargs = super(ReviewCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


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


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('book_list')
    login_url = reverse_lazy('account_login')
    context_object_name = 'review'
    template_name = 'reviews/review_confirm_delete.html'
