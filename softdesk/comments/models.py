import uuid

from django.conf import settings
from django.db import models

from issues.models import Issue


class Comment(models.Model):

    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_author'
    )
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='issue_comment',
    )
    description = models.TextField(max_length=2048)
    created_time = models.DateTimeField(auto_now_add=True)
