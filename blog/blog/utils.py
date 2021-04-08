# Import modules
from django.core.paginator import Paginator

# Create function to pagniate articles
def pagniate_articles(page_number, obj):
    paginator = Paginator(obj, 5)
    page_obj = paginator.get_page(page_number)
    return page_obj