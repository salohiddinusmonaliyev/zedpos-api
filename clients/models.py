from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(("Ism"), max_length=50)
    last_name = models.CharField(("Familya"), max_length=50)
    p_num = models.CharField(("Telefon raqami"), max_length=20)
    qarz = models.IntegerField(("Qarz"), null=True, blank=True, default=0)

    class Meta:
        verbose_name = ('Mijoz')
        verbose_name_plural = ('Mijozlar')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
