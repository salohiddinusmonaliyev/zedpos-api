from rest_framework.serializers import ModelSerializer

from .models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class NewProductSerializer(ModelSerializer):
    class Meta:
        model = NewProduct
        fields = "__all__"
