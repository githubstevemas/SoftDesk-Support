from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from issues.models import Issue


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
    # Allow to update author and check if in contributors

    class Meta:
        model = Issue
        fields = ['author']

    def validate_author(self, value):
        request = self.context.get('request')
        if request:
            project = self.instance.project
            if (value != project.author
                    and value not in project.contributors.all()):
                raise ValidationError(
                    "Must be the project author or a project contributor."
                )
        return value
