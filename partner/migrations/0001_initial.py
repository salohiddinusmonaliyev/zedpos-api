# Generated by Django 4.1.7 on 2023-02-14 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DealerOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('dealer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partner.dealer')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
