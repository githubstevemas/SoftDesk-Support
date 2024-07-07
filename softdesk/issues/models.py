from django.conf import settings
from django.db import models

from projects.models import Project


class Issue(models.Model):

    class Priority(models.TextChoices):
        LOW = "low"
        MEDIUM = "medium"
        HIGH = "high"

    class Type(models.TextChoices):
        BUG = "bug"
        FEATURE = "feature"
        TASK = "task"

    class Status(models.TextChoices):
        TO_DO = "to do"
        IN_PROGRESS = "in progress"
        FINISHED = "finished"

    name = models.CharField(max_length=128)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_issue',
    )
    description = models.TextField(max_length=2048)
    priority = models.CharField(choices=Priority.choices, max_length=6)
    type = models.CharField(choices=Type.choices, max_length=7)
    status = models.CharField(choices=Status.choices, max_length=11)
    created_time = models.DateTimeField(auto_now_add=True)
