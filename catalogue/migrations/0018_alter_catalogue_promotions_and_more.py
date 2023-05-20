# Generated by Django 4.2.1 on 2023-05-19 20:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_alter_catalogue_prix_alter_promo_promo_date_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='promotions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.promo'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 19, 22, 4, 27, 833998), null=True, verbose_name='DATE FIN'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 19, 22, 4, 27, 833998), null=True, verbose_name='DATE DEBUT'),
        ),
    ]