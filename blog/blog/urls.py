# Import modules
from django.urls import path

from .views import index

app_name = "blog"

# Register views / urls
urlpatterns = [
    path('', index, name='index'),
]
