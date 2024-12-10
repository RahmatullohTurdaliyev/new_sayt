from django.contrib import admin
from .models import Category, News

# admin.site.register(News)
# admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'published_time')
    list_filter = ('status', 'created_time', 'published_time', 'category')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    date_hierarchy = 'created_time'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

