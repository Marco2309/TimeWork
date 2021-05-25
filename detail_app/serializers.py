from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from detail_app.models import Detail


class DetailViewSerializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'
