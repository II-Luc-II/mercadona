# Generated by Django 4.2.1 on 2023-05-18 10:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_remove_catalogue_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.categories', verbose_name='CATEGORIES'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categories',
            field=models.CharField(blank=True, max_length=60, verbose_name='CATEGORIE'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 12, 26, 58, 939602), verbose_name='DATE FIN'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 12, 26, 58, 939602), null=True, verbose_name='DATE DEBUT'),
        ),
    ]