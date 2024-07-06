from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from softdesk.permissions import IsSuperUser, IsSelf
from users.serializers import UsersSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action == 'list':
            return [IsSuperUser()]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsSelf()]
        return super(UserViewSet, self).get_permissions()
