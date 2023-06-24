# Generated by Django 4.2.1 on 2023-06-14 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_remove_catalogue_promotions_catalogue_promotions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogue',
            name='promotions',
        ),
        migrations.AddField(
            model_name='catalogue',
            name='promotions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.promo'),
        ),
    ]
