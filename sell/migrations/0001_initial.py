# Generated by Django 4.1.4 on 2022-12-26 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Vaqt')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Mijoz')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ishchi')),
            ],
            options={
                'verbose_name': 'Sotildi',
                'verbose_name_plural': 'Sotilganlar',
            },
        ),
        migrations.CreateModel(
            name='SellItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Mahsulot')),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.sell')),
            ],
            options={
                'verbose_name': 'SellItem',
                'verbose_name_plural': 'SellItems',
            },
        ),
    ]
