# Generated by Django 4.2.1 on 2023-05-18 10:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_remove_catalogue_promotions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogue',
            name='categories',
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 12, 17, 31, 488612), verbose_name='DATE FIN'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 12, 17, 31, 488612), null=True, verbose_name='DATE DEBUT'),
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.catalogue', verbose_name='CATEGORIES')),
            ],
        ),
    ]
