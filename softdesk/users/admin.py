from django.contrib import admin

from users.models import User, Contributor


admin.site.register(User)
admin.site.register(Contributor)
