from django.db import models
from clients.models import Client

from product.models import Product

# Create your models here.
class Sell(models.Model):
    client = models.ForeignKey(Client, verbose_name=("Mijoz"), on_delete=models.CASCADE, null=True, blank=True)
    vaqti = models.DateTimeField(("Vaqt"))
    total_price = models.IntegerField(null=True, blank=True, default=0)
    desc = models.TextField(null=True, blank=True)
    worker = models.ForeignKey("accounts.CustomUser", verbose_name=("Ishchi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Sotildi")
        verbose_name_plural = ("Sotilganlar")

    def __str__(self):
        return f"{self.id}"

class SellItem(models.Model):
    sell_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name=("Mahsulot"), on_delete=models.SET_NULL, null=True)
    chegirma = models.IntegerField(("Bitta mahsulot uchun chegirma"),null=True, default=0)
    date = models.DateTimeField(null=True)
    quantity = models.IntegerField(null=True)

    class Meta:
        verbose_name = ("SellItem")
        verbose_name_plural = ("SellItems")

    def __str__(self):
        return f"{self.id} {self.product_id.name} {self.sell_id.vaqti}"

class HarajatCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Harajat(models.Model):
    ishchi_id = models.ForeignKey('accounts.CustomUser', verbose_name="Ishchi", on_delete=models.CASCADE)
    sabab = models.ForeignKey(HarajatCategory, on_delete=models.CASCADE)
    date = models.DateTimeField()
    pul = models.IntegerField(("Ishlatilgan pul"))

    def __str__(self):
        return f"{self.ishchi_id.username} | {self.pul}"

    class Meta:
        verbose_name = 'Harajat'
        verbose_name_plural = 'Harajatlar'
