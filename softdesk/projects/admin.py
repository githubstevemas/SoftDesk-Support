from django.contrib import admin

from projects.models import Project, Issue, Comment


admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
