# Import modules
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Article

# Create view for blog index
def index(request):
    context = {
        'articles': Article.objects.filter(status='p').order_by('-publish')
    }
    return render(request, 'blog/index.html', context)


# Create view for article content
def article_content(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/post.html', context)
