from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskViewSeralizer
from .permissions import TaskPermissions

# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskViewSeralizer
    permission_classes = (TaskPermissions,)

    def get_queryset(self):
        id_user = self.request.user.id
        my_tasks = self.queryset.filter(user_id=id_user)
        return my_tasks