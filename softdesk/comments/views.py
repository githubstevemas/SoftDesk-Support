from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.serializers import CommentsSerializer
from issues.models import Issue
from softdesk.permissions import IsAuthorOrContributor, IsAuthor


class CommentsViewset(ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):

        # Get comments for project_id and issue_id
        issue_id = self.kwargs.get('issue_id')
        project_id = self.kwargs.get('project_id')
        return Comment.objects.filter(
            issue_id=issue_id,
            issue__project_id=project_id
        )

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

        # Set issue and author
        issue_id = self.kwargs.get('issue_id')
        issue = Issue.objects.get(id=issue_id)
        serializer.save(author=self.request.user, issue=issue)
