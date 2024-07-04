from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issue, Comment
from projects.serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer
from softdesk.permissions import IsAuthor, IsAuthorized


class ProjectsViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)


class IssuesViewset(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthorized]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthorized]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
