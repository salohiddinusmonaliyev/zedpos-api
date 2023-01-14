from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import *
from clients.models import *
from sell.models import *

# Create your views here.
class HomeView(APIView):
    def get(self, request,a, b):
        # Umumiy sonlar
        products = Product.objects.filter(is_active=True).count()
        clients = Client.objects.all().count()
        qarzdorlar = Client.objects.filter(qarz__lte=0).count()

        # sotuv
        sotuv = []

        # daromad
        d = Sell.objects.all()
        daromad = 0
        for u in d:
            if str(u.vaqti.date())>=a and str(u.vaqti.date())<=b:
                daromad = int(daromad)+int(u.total_price)
                sotuv.append(d)
        sotuv = len(sotuv)

        # foyda
        data = SellItem.objects.filter()
        foyda = 0
        for i in data:
            if str(i.date.date()) >= a and str(i.date.date()) <= b:
                product_price = (int(i.quantity)*i.product_id.price) - (int(i.quantity)*int(i.chegirma))
                product_kelgan = (int(i.quantity)*i.product_id.kelgan_narx)
                foyda = foyda + (product_price-product_kelgan)

        # harajat
        h = Harajat.objects.all()
        harajat = 0
        for ha in h:
            if str(ha.date.date()) >= a and str(ha.date.date()) <= b:
                harajat = harajat + ha.pul

        # top 5 mahsulotlar
        sellitems = SellItem.objects.all()

        # tashqi haqlarsli
        qarzlar = Client.objects.all()
        qarz = 0
        for q in qarzlar:
            qarz=qarz+q.qarz

        # do'kondagi tovarlar
        t = Product.objects.all()
        tovarlar = 0
        for y in t:
            tovarlar = tovarlar + y.kelgan_narx

        # 10 tadan kam qolgan
        product = Product.objects.filter(is_active=True, nechta__lte=10)
        return Response(sotuv)