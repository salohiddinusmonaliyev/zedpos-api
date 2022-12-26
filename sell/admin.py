from django.contrib import admin

from .models import Sell, SellItem

# Register your models here.
admin.site.register(Sell)
admin.site.register(SellItem)
