from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['story', 'user', 'rating', 'bias', 'created_at']
    list_filter = ['rating', 'bias', 'created_at']
    search_fields = ['story__title', 'user__username', 'comment']
    ordering = ['-created_at']