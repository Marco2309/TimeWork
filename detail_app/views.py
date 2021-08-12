from django.core.checks import messages
from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from detail_app.models import Detail
from detail_app.serializers import DetailViewSerializer
from .permissions import DetailPermissions
from task_app.models import Task
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
# maybe will be best if add  a table of sub details

class DetailViewSet(ModelViewSet):
    serializer_class = DetailViewSerializer
    queryset = Detail.objects.all()
    permission_classes = (DetailPermissions,)

    def get_queryset(self):
        id_user = self.request.user.id
        my_tasks = Task.objects.filter(user_id=id_user)
        my_details = self.queryset.filter(task_id__in=my_tasks)
        return my_details

    def create(self, request, *args, **kwargs):
        data = request.data
        id_user = self.request.user.id
        my_tasks = Task.objects.filter(user_id=id_user)
        my_details = my_tasks.filter(id=data['task'])
        if my_details:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"messages":"task not found"})

    def perform_create(self, serializer):
        serializer.save()
