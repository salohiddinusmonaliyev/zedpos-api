from rest_framework.serializers import ModelSerializer

from .models import *

class ReturnedSerializer(ModelSerializer):
    class Meta:
        model = Returned
        fields = "__all__"
