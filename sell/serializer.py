from rest_framework.serializers import ModelSerializer

from .models import *

class SellSerializer(ModelSerializer):
    class Meta:
        model = Sell
        fields = "__all__"


class SellItemSerializer(ModelSerializer):
    class Meta:
        model = SellItem
        fields = "__all__"

class HarajatSerializer(ModelSerializer):
    class Meta:
        model = Harajat
        fields = "__all__"