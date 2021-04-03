# Import modules
from django.urls import path

from .views import index, article_content

app_name = "blog"

# Register views / urls
urlpatterns = [
    path('', index, name='index'),
    path('blog/<slug:slug>', article_content, name='article_content')
]
