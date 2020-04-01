from django.urls import path

from .views import HomePageView, AboutPageView

# register a namespace
app_name = 'pages'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
