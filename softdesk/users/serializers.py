from rest_framework.serializers import ModelSerializer
from .models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            # 'birthdate',
            'can_be_contacted',
            'can_data_be_shared',
            'password'
        ]

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            # birthdate=validated_data['birthdate'],
            can_be_contacted=validated_data['can_be_contacted'],
            can_data_be_shared=validated_data['can_data_be_shared'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
