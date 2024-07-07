from rest_framework.serializers import ModelSerializer

from comments.models import Comment
# from issues.serializers import IssuesSerializer
# from users.serializers import UsersSerializer


class CommentsSerializer(ModelSerializer):
    # author = UsersSerializer(read_only=True)
    # issue = IssuesSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'issue',
            'description',
            'created_time'
        ]
        extra_kwargs = {
            'issue': {'required': False}
        }
        read_only_fields = ['author']
