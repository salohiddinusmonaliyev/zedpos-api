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

class HarajatViewSet(ModelViewSet):
    queryset = Harajat.objects.all()
    serializer_class = HarajatSerializer

class Tolov(APIView):

    def get(self, request, a):
        s = Sell.objects.get(id=a)
        data = SellItem.objects.filter(sell_id=s)
        products = ""
        summa = 0
        for i in data:
            total = (int(i.product_id.price)*int(i.quantity))+summa
            foyda = (int(i.product_id.kelgan_narx) * int(i.quantity))
            foyda = total - foyda
            chegirma = 0
            products = products+f"{i.quantity} {i.product_id.ulchovi} {i.product_id.name}"+", "
            summa = total
            if i.chegirma!=0:
                chegirma = int(i.quantity)*int(chegirma+i.chegirma)
            else:
                chegirma = 0
        s.total_price = total
        s.save()
        print("--------------")
        aa = request.data.get("salom")
        print(aa)
        print("--------------")

        return Response(f"Olingan mahsulotlar: {products}; Umumiy hisob: {total}; So'ngi hisob: {summa-chegirma}; Chegirmasiz foyda: {foyda}; Chegirmali foyda: {foyda-chegirma};", status=status.HTTP_200_OK)
