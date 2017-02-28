from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
