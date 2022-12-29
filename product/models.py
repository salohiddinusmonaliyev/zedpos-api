from django.db import models

from partner.models import Partner

# Create your models here.
class Product(models.Model):
    title = models.CharField(("Mahsulot nomi"), max_length=50)
    hajmi = models.CharField(("Bitta mahsulot hajmi"), max_length=20)
    nechta = models.IntegerField(("Mahsulot nechta"))
    narx = models.IntegerField(("Narxi"))

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return self.title

class NewProduct(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Hamkor")
    date = models.DateField(("Sana"))
    nechta = models.IntegerField(("Mahsulot nechta"), null=True)
    bir_hajmi = models.CharField(("Bitta mahsulot hajmi"), max_length=50)
    bir_narx = models.IntegerField(("Bitta mahsulot narxi"))
    sotiladigan = models.IntegerField(("Sotiladigan narxi"))
    um_narx = models.IntegerField(("Umumiy narx"))
    tolandi = models.BooleanField(("Umumiy pul to'landimi"),null=True)
    qancha = models.IntegerField(("Qancha pul to'landi"),null=True)

    class Meta:
        verbose_name = 'Yangi mahsulot'
        verbose_name_plural = 'Yangi mahsulotlar'

    def __str__(self):
        return self.partner.name
