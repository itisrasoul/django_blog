# Import modules
from django.contrib import admin

from .models import Article, Category



# Register models
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', 'category_to_str')
    ordering = ['-publish', 'status']
    list_filter = ('publish', 'status')
    search_fields = ('title', 'publish', 'description')
    prepopulated_fields = {'slug': ('title',)}

    def category_to_str(self, article):
        return ", ".join([category.title for category in article.category.all()])
    category_to_str.short_description = 'دسته بندی'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', )
    ordering = ['title', 'status']
    list_filter = (['status'])
    search_fields = ('title', 'description', 'position')
    prepopulated_fields = {'slug': ('title',)}



# Use this instead of decorator if you don't have any admin page customizations :
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Category, CategoryAdmin)
