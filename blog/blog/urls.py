# Import modules
from django.urls import path

from .views import index, article_content, about_us, contact_us

app_name = "blog"

# Register views / urls
urlpatterns = [
    path('', index, name='index'),
    path('blog/<slug:slug>', article_content, name='article_content'),
    path('about_us/', about_us, name='about_us'),
    path('contact_us/', contact_us, name='contact_us')
]
