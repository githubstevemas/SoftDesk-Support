from rest_framework import permissions
from rest_framework.exceptions import NotFound

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


class IsAuthorOrContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_id')
        if project_id:
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                raise NotFound(detail="Project not found.")
            return (
                request.user == project.author or
                request.user in project.contributors.all()
            )
        return False

class IsNotAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_authenticated
