from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskViewSeralizer
from .permissions import TaskPermissions
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskViewSeralizer
    permission_classes = (TaskPermissions,)

    def get_queryset(self):
        id_user = self.request.user.id
        my_tasks = self.queryset.filter(user_id=id_user)
        return my_tasks

    def create(self, request, *args, **kwargs):
        if request.auth == None:
            return Response(data={"message: You need to register"}, status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
