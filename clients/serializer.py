from rest_framework.serializers import ModelSerializer

from .models import *

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
