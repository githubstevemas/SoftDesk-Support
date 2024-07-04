from rest_framework import permissions

from projects.models import Project


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsAuthorized(permissions.BasePermission):

    def has_permission(self, request, view):
        project_id = request.data.get('project')
        if not project_id:
            return False

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return False

        return request.user == project.author or request.user in project.contributors.all()
