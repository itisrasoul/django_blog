# Import modules
from django.urls import path

from .views import index

# Register views / urls
urlpatterns = [
    path('', index),
]
