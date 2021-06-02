from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import UserViewSerializer, PartialUserViewSerializer
from .permissions import UserPermissions
# Create your views here.


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
    permission_classes = (UserPermissions,)

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return PartialUserViewSerializer
        return super().get_serializer_class()
