# Import modules
from django import template

from ..models import Category

# Register template tag
register = template.Library()

@register.inclusion_tag("blog/partials/category_navbar.html")
def categories():
    return {
        'categories': Category.objects.filter(status=True)
    }