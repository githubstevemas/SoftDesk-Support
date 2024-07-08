from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from comments.models import Comment
from comments.serializers import CommentsSerializer
from issues.models import Issue
from softdesk.permissions import IsAuthorOrContributor, IsAuthor


class CommentsViewset(ModelViewSet):
    serializer_class = CommentsSerializer

    def get_issue(self):
        issue_id = self.kwargs.get('issue_id')
        project_id = self.kwargs.get('project_id')
        try:
            return Issue.objects.get(id=issue_id, project_id=project_id)
        except Issue.DoesNotExist:
            raise NotFound(detail="Issue not found.")

    def get_queryset(self):
        issue = self.get_issue()
        return Comment.objects.filter(issue=issue).order_by('id')

    def get_permissions(self):
        """
        Allow author or contributors of the project to list or create
        Only author can update or destroy
        """
        if self.action in ['create', 'list']:
            self.permission_classes = [IsAuthorOrContributor]
        elif self.action in [
            'retrieve',
            'update',
            'partial_update',
            'destroy'
        ]:
            self.permission_classes = [IsAuthor]
        return super(CommentsViewset, self).get_permissions()

    def perform_create(self, serializer):
        issue = self.get_issue()
        serializer.save(author=self.request.user, issue=issue)
