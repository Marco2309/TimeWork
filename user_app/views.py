from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import UserViewSerializer, PartialUserViewSerializer
from .permissions import UserPermissions
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
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


@api_view(['POST'])
def usernameOfEmail(request):
    try:
        email = request.data['email']
        user = User.objects.get(email=email)
        return Response(status=status.HTTP_200_OK, data={'user': f'{user.username}',
        'id': f'{user.id}'})
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
