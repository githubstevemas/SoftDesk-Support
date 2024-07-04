import uuid

from django.conf import settings
from django.db import models


class Project(models.Model):

    class Type(models.TextChoices):
        BACK_END = "back"
        FRONT_END = "front"
        IOS = "ios"
        ANDROID = "android"

    name = models.CharField(max_length=128)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_author'
    )
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='project_contributors',
        blank=True
    )
    description = models.TextField(max_length=2048)
    type = models.CharField(choices=Type.choices, max_length=7)
    created_time = models.DateTimeField(auto_now_add=True)


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
    # issue_link = ???
    description = models.TextField(max_length=2048)
    created_time = models.DateTimeField(auto_now_add=True)
