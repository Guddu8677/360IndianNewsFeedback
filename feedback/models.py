from django.db import models
from django.conf import settings

class Feedback(models.Model):
    BIAS_CHOICES = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
        ('unknown', 'Unknown')
    ]
    
    story = models.ForeignKey('stories.NewsStory', on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.IntegerField()
    bias = models.CharField(max_length=50, choices=BIAS_CHOICES, default='unknown')
    accuracy_flag = models.BooleanField(default=False)
    tags = models.JSONField(default=list, blank=True)
    comment = models.TextField(blank=True)
    sentiment = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=10, default='en')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        user_name = self.user.username if self.user else "Anonymous"
        return f"Feedback by {user_name} on {self.story.title[:50]}"