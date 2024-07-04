from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from projects.models import Project


class User(AbstractUser):
    birthdate = models.DateField()
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)


class Contributor(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')
