from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from sell.models import *
from sell.serializer import SellItemSerializer
from .models import Returned
from .serializer import ReturnedSerializer


# Create your views here.
class ReturnedViewSet(ModelViewSet):
    queryset = Returned.objects.all()
    serializer_class = ReturnedSerializer

