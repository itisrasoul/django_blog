# Import modules
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Category, About, Article
from .utils import pagniate_articles


# Create view for blog index
def index(request):
    articles_list = Article.objects.published_articles()
    page_number = request.GET.get('page')
    page_obj = pagniate_articles(page_number, articles_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


# Create view for article content
def article_content(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/post.html', context)

# Create view for about us content
def about_us(request):
    context = {
        'about': About.objects.first(),
    }
    return render(request, 'blog/about.html', context)


# Create view for contact us content
def contact_us(request):
    context = {
        'contact': About.objects.first(),
    }
    return render(request, 'blog/contact.html', context)


# Create view for category articles
def category(request, slug):
    category_object = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category_object.articles.published_articles()
    page_number = request.GET.get('page')
    page_obj = pagniate_articles(page_number, articles_list)
    context = {
        'page_obj': page_obj,
        'category': category_object,
    }
    return render(request, 'blog/category.html', context)