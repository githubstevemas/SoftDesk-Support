from rest_framework.serializers import ModelSerializer

from projects.models import Project
# from users.serializers import UsersSerializer


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
        extra_kwargs = {
            'author': {'required': False}
        }
        read_only_fields = ['author', 'project']
