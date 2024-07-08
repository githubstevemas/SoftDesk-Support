from rest_framework.viewsets import ModelViewSet

from softdesk.permissions import IsSuperUser, IsSelf, IsNotAuthenticated
from users.serializers import UsersSerializer
from .models import User


class UserViewSet(ModelViewSet):
    # Define queryset to get all Users objects and specify the serializer
    queryset = User.objects.all().order_by('id')
    serializer_class = UsersSerializer

    def get_permissions(self):
        """
        Allow any user to create
        Only superuser can list users
        Only users themselves can update and destroy their account
        """

        if self.action == 'create':
            return [IsNotAuthenticated()]
        elif self.action == 'list':
            return [IsSuperUser()]
        elif self.action == 'retrieve':
            return [IsSuperUser()]
        elif self.action in [
            'update',
            'partial_update',
            'destroy'
        ]:
            return [IsSelf()]
        return super(UserViewSet, self).get_permissions()
