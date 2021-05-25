from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from detail_app.models import Detail
from detail_app.serializers import DetailViewSerializer

# Create your views here.


class DetailViewSet(ModelViewSet):
    serializer_class = DetailViewSerializer
    queryset = Detail.objects.all()

    
