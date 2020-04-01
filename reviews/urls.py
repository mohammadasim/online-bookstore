from django.urls import path

from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

# register a namespace
app_name = 'reviews'

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='review_create'),
    path('<uuid:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('<uuid:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),

]
