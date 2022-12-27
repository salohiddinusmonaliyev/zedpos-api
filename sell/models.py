from django.db import models
from clients.models import Client

from product.models import Product

# Create your models here.
class Sell(models.Model):
    client = models.ForeignKey(Client, verbose_name=("Mijoz"), on_delete=models.CASCADE)
    date = models.DateTimeField(("Vaqt"), auto_now=True)
    worker = models.ForeignKey("accounts.CustomUser", verbose_name=("Ishchi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Sotildi")
        verbose_name_plural = ("Sotilganlar")

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name}"

class SellItem(models.Model):
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Mahsulot"), on_delete=models.CASCADE)
    price = models.IntegerField(("Sotilgan narx"))


    class Meta:
        verbose_name = ("SellItem")
        verbose_name_plural = ("SellItems")

    def __str__(self):
        return f"{self.sell.client} {self.sell.date}"
