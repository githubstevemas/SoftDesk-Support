from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue, Comment
from users.serializers import UsersSerializer


class ProjectsSerializer(ModelSerializer):
    # author = UsersSerializer(read_only=True)
    # contributors = UsersSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'author',
            'contributors',
            'description',
            'type',
            'created_time'
        ]


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'id',
            'name',
            'author',
            'project',
            'description',
            'priority',
            'type',
            'status',
            'created_time'
        ]
        extra_kwargs = {
            'project': {'required': False}
        }
        read_only_fields = ['author', 'project']


class IssueUpdateAuthorSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['author']

    def validate_author(self, value):
        request = self.context.get('request')
        if request:
            project = self.instance.project
            if value != project.author and value not in project.contributors.all():
                raise ValidationError(
                    "Must be the project author or a project contributor."
                )
        return value


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
