# Import modules
from django.contrib import admin

from .models import Article

# Register models
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', )
    ordering = ['-publish', 'status']
    list_filter = ('publish', 'status')
    search_fields = ('title', 'publish', 'description')
    prepopulated_fields = {'slug': ('title',)}


# Use this instead of decorator if you don't have any admin page customizations :
# admin.site.register(Article, ArticleAdmin)