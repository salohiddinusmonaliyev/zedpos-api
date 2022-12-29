from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Returned
from .serializer import ReturnedSerializer

# Create your views here.
class ReturnedViewSet(ModelViewSet):
    queryset = Returned.objects.all()
    serializer_class = ReturnedSerializer