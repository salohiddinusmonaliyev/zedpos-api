from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.CharField(("Firma nomi"), max_length=50)
    qarz = models.IntegerField(("Do'kon qarzi"), null=True, blank=True, default=True)

    class Meta:
        verbose_name = ("Hamkor")
        verbose_name_plural = ("Hamkorlar")

    def __str__(self):
        return self.name
