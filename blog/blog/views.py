#Import modules
from django.shortcuts import render
# from django.http import HttpResponse

from .models import Article

# Create your views here.
def index(request):
    context = {
        'articles': Article.objects.filter(status='p').order_by('-publish')
    }
    return render(request, 'blog/index.html', context)

def article_content(request, slug):
    context = {
        'article': Article.objects.get(slug=slug)
    }
    return render(request, 'blog/post.html', context)