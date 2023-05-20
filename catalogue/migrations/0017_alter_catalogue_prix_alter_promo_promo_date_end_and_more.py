# Generated by Django 4.2.1 on 2023-05-18 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_alter_catalogue_promotions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='PRIX €'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 19, 31, 2, 556163), null=True, verbose_name='DATE FIN'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 19, 31, 2, 556163), null=True, verbose_name='DATE DEBUT'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_prix',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='PRIX €'),
        ),
    ]
