from django.db import models

from partner.models import Partner

# Create your models here.
class Product(models.Model):
    kod = models.IntegerField(max_length=10000, null=True)
    name = models.CharField(("Mahsulot nomi"), max_length=50)
    kelgan_narx = models.IntegerField(("Kelgan narxi"))
    price = models.IntegerField(("Narxi"))
    ulchovi = models.CharField(max_length=20, null=True, blank=True)
    nechta = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return self.name

class NewProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    hamkor_id = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Hamkor")
    date = models.DateField(("Sana"))
    nechta = models.IntegerField(("Mahsulot nechta"), null=True)
    bir_hajmi = models.CharField(("Bitta mahsulot hajmi"), max_length=50)
    # bir_narx = models.IntegerField(("Bitta mahsulot narxi"))
    # sotiladigan = models.IntegerField(("Sotiladigan narxi"))
    um_narx = models.IntegerField(("Umumiy narx"))

    class Meta:
        verbose_name = 'Yangi mahsulot'
        verbose_name_plural = 'Yangi mahsulotlar'

    def __str__(self):
        return self.partner.name
