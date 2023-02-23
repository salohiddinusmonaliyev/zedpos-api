from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import generics, status

from .serializer import *
from .models import *

# Create your views here.
class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class SellItemViewSet(ModelViewSet):
    queryset = SellItem.objects.all()
    serializer_class = SellItemSerializer

class CostViewSet(ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

class Payment(APIView):

    def get(self, request, a):
        s = Sell.objects.get(id=a)
        data = SellItem.objects.filter(sell_id=s)
        products = ""
        summa = 0
        for i in data:
            total = (int(i.product_id.price)*int(i.quantity))+summa
            foyda = (int(i.product_id.incoming_price) * int(i.quantity))
            foyda = total - foyda
            discount = 0
            products = products+f"{i.quantity} {i.product_id.measure} {i.product_id.name}"+", "
            summa = total
            if i.discount!=0:
                discount = int(i.quantity)*int(discount+i.discount)
            else:
                discount = 0
        s.total_price = total
        s.save()

        return Response(f"Olingan mahsulotlar: {products}; Umumiy hisob: {total}; So'ngi hisob: {summa-discount}; Chegirmasiz foyda: {foyda}; Chegirmali foyda: {foyda-discount};", status=status.HTTP_200_OK)
