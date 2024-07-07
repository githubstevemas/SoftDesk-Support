from datetime import date

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, Contributor


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'birthdate',
            'can_be_contacted',
            'can_data_be_shared',
            'password'
        ]

    def validate_birthdate(self, value):
        # check if user is over 15

        today = date.today()
        age = today.year - value.year - (
                    (today.month, today.day) < (value.month, value.day))
        if age < 15:
            raise serializers.ValidationError(
                "User must be at least 15 years old.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            birthdate=validated_data['birthdate'],
            can_be_contacted=validated_data['can_be_contacted'],
            can_data_be_shared=validated_data['can_data_be_shared'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            'user',
            'project'
        ]
