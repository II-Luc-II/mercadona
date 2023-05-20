# Generated by Django 4.2.1 on 2023-05-19 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_alter_promo_promo_date_end_alter_promo_promo_date_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promo_date_end',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='DATE FIN'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_date_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='DATE DEBUT'),
        ),
    ]
