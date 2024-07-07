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
