from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.TextField(
        null=True,
        blank=True,
    )
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_updated(self) -> bool:
        return self.updated_at - self.inserted_at > timedelta(minutes=1)
