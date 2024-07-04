from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issue, Comment
from projects.serializers import (
    ProjectsSerializer,
    IssuesSerializer,
    CommentsSerializer
)
from softdesk.permissions import IsAuthor, IsAuthorOrContributor


class ProjectsViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in [
            'retrieve', 'update', 'partial_update', 'destroy'
        ]:
            self.permission_classes = [IsAuthor]
        return super(ProjectsViewset, self).get_permissions()

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)


class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Issue.objects.filter(project_id=project_id)

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthorOrContributor]
        elif self.action in [
            'retrieve', 'update', 'partial_update', 'destroy'
        ]:
            self.permission_classes = [IsAuthor]
        return super(IssuesViewset, self).get_permissions()

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)
        serializer.save(author=self.request.user, project=project)


class CommentsViewset(ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        return Comment.objects.filter(issue_id=issue_id)

    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthorOrContributor]
        elif self.action in [
            'retrieve', 'update', 'partial_update', 'destroy'
        ]:
            self.permission_classes = [IsAuthor]
        return super(CommentsViewset, self).get_permissions()

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_id')
        issue = Issue.objects.get(id=issue_id)
        serializer.save(author=self.request.user, issue=issue)
