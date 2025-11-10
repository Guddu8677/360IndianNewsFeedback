from django.db import models
from django.utils import timezone

class NewsStory(models.Model):
    title = models.CharField(max_length=500)
    source = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    published_at = models.DateTimeField(default=timezone.now)
    summary = models.TextField()
    content = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    sentiment = models.CharField(max_length=20, blank=True)
    keywords = models.JSONField(default=list, blank=True)
    image_url = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    is_live = models.BooleanField(default=False)  # True for API news, False for manual entries
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "News Stories"
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title