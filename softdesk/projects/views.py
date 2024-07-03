from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issue, Comment
from projects.serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(f"Current user: {user}")
        print(f"Request headers: {self.request.headers}")
        return Project.objects.all()


class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentsViewset(ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comment.objects.all()
