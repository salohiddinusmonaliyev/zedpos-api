from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.CharField(("Firma nomi"), max_length=50)
    p_num = models.CharField(max_length=50, null=True)
    class Meta:
        verbose_name = ("Hamkor")
        verbose_name_plural = ("Hamkorlar")

    def __str__(self):
        return self.name

class PartnerChiqim(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    worker = models.ForeignKey("accounts.CustomUser", on_delete=models.SET_NULL, null=True)
    desc = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Hamkorga berilgan pul")