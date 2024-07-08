from rest_framework.viewsets import ModelViewSet

from issues.models import Issue
from issues.serializers import IssueUpdateAuthorSerializer, IssuesSerializer
from projects.models import Project
from softdesk.permissions import IsAuthorOrContributor, IsAuthor


class IssuesViewset(ModelViewSet):

    def get_serializer_class(self):

        # Specify the serializer if author or not
        if self.action in ['update',
                           'partial_update'] and 'author' in self.request.data:
            return IssueUpdateAuthorSerializer
        return IssuesSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Issue.objects.filter(project_id=project_id).order_by('id')

    def get_permissions(self):
        """
        Allow author or contributors of the project to list or create
        Only author can update or destroy
        """
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthorOrContributor]
        elif self.action in ['retrieve',
                             'update',
                             'partial_update',
                             'destroy']:
            self.permission_classes = [IsAuthor]
        return super(IssuesViewset, self).get_permissions()

    def perform_create(self, serializer):

        # Set author as curent user and add it to contributors list
        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)
        serializer.save(author=self.request.user, project=project)
