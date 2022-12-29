from django.db import models
from clients.models import Client

from product.models import Product

# Create your models here.
class Sell(models.Model):
    client = models.ForeignKey(Client, verbose_name=("Mijoz"), on_delete=models.CASCADE)
    date = models.DateField(("Vaqt"), auto_now=True)
    worker = models.ForeignKey("accounts.CustomUser", verbose_name=("Ishchi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Sotildi")
        verbose_name_plural = ("Sotilganlar")

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name}"

class SellItem(models.Model):
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Mahsulot"), on_delete=models.CASCADE)
    price = models.IntegerField(("Sotilgan narx"), null=True)

    class Meta:
        verbose_name = ("SellItem")
        verbose_name_plural = ("SellItems")

    def __str__(self):
        return f"{self.price} | {self.sell.client.first_name} {self.sell.client.last_name}-{self.sell.date}"

class Harajat(models.Model):
    ishchi = models.ForeignKey('accounts.CustomUser', verbose_name="Ishchi", on_delete=models.CASCADE)
    sabab = models.CharField(("Sababi"), max_length=100)
    pul = models.IntegerField(("Ishlatilgan pul"))

    def __str__(self):
        return f"{self.ishchi.username} | {self.pul}"

    class Meta:
        verbose_name = 'Harajat'
        verbose_name_plural = 'Harajatlar'
