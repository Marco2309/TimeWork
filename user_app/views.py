from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from user_app.serializers import UserViewSerializer
# Create your views here.


class UserViewSet(ModelViewSet):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
