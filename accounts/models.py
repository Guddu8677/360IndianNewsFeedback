# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # extend later (phone, role, region, language)
    region = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=10, default='en')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="accounts_user_set", # ADDED THIS LINE
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="accounts_user_set",  # ADDED THIS LINE
        related_query_name="user",
    )



    def __str__(self):
        return self.username  # Display username in admin panel and other places