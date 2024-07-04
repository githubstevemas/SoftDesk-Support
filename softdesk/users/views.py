from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from softdesk.permissions import IsSuperUser, IsSelf
from .models import User
from .serializers import UsersSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsSuperUser]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        if self.action == 'list':
            self.permission_classes = [IsSuperUser]
        elif self.action in ['retrieve',
                             'update',
                             'partial_update',
                             'destroy'
                             ]:
            self.permission_classes = [IsSelf]
        return super(UserViewSet, self).get_permissions()
