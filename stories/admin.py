from django.contrib import admin
from .models import NewsStory

@admin.register(NewsStory)
class NewsStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'is_live', 'published_at', 'created_at']
    search_fields = ['title', 'source', 'content']
    list_filter = ['source', 'is_live', 'published_at', 'category']
    ordering = ['-published_at']
    readonly_fields = ['created_at']