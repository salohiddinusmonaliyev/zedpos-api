from django.db import models
from accounts.models import CustomUser

from clients.models import Client
from sell.models import Sell

# Create your models here.
class Returned(models.Model):
    client = models.ForeignKey(Client, verbose_name=("Mijoz"), on_delete=models.CASCADE)
    sellitem = models.ForeignKey(Sell, verbose_name=("Sell Item") , on_delete=models.CASCADE)
    price = models.IntegerField(("Berilgan Pul"))
    worker = models.ForeignKey(CustomUser, verbose_name=("Ishchi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Qaytarilgan Mahsulot")
        verbose_name_plural = ("Qaytarilgan Mahsulotlar")

    def __str__(self):
        return self.mijoz_id.first_name