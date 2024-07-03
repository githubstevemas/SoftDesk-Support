from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue, Comment


class ProjectsSerializer(ModelSerializer):

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
            'contributors',
            'description',
            'priority',
            'type',
            'status',
        ]


class CommentsSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'issue',
            'description',
        ]
