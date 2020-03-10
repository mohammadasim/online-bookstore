from django.urls import path

from .views import ReviewCreateView, ReviewUpdateView

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='review_create'),
    path('update/<uuid:pk>', ReviewUpdateView.as_view(), name='review_update'),

]
