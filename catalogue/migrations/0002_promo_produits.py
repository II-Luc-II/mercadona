# Generated by Django 4.2.1 on 2023-06-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='produits',
            field=models.CharField(blank=True, max_length=60, verbose_name='PRODUITS'),
        ),
    ]
