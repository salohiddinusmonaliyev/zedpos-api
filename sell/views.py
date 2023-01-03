from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializer import *
from .models import *

# Create your views here.
class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class SellItemViewSet(ModelViewSet):
    queryset = SellItem.objects.all()
    serializer_class = SellItemSerializer

class HarajatViewSet(ModelViewSet):
    queryset = Harajat.objects.all()
    serializer_class = HarajatSerializer
# shu bilan boldimi boshga heshnima kerak emas togrimi?    
