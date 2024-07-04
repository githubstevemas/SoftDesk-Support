from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue, Comment
from users.models import User
from users.serializers import UsersSerializer


class ProjectsSerializer(ModelSerializer):
    author = UsersSerializer(read_only=True)
    contributors = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

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
    author = UsersSerializer(read_only=True)

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
        ]


class CommentsSerializer(ModelSerializer):
    author = UsersSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'issue',
            'description',
        ]
