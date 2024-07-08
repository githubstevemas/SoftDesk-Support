from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import (ProjectsSerializer)
from softdesk.permissions import IsAuthor


class ProjectsViewset(ModelViewSet):
    # Define queryset to get all Users objects and specify the serializer
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectsSerializer

    def get_permissions(self):
        """
        Authenticated users can create and list projects
        Only authors can update or destroy thier projects
        """

        if self.action in ['list']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in [
            'retrieve',
            'update',
            'partial_update',
            'destroy'
        ]:
            self.permission_classes = [IsAuthor]
        return super(ProjectsViewset, self).get_permissions()

    def perform_create(self, serializer):
        # Set author as curent user and add it to contributors list
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)

    def perform_update(self, serializer):
        # Add request user to contributors if update
        instance = serializer.save()
        if instance.author not in instance.contributors.all():
            instance.contributors.add(instance.author)
