# Import modules
from django.contrib import admin

from .models import Article

# Register models
admin.site.register(Article)