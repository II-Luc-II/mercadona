from django.db import models
from django.utils import timezone


# Create your models here.
class Catalogue(models.Model):

    categories = models.ForeignKey('Categories', null=True, verbose_name="CATEGORIES", on_delete=models.CASCADE)
    produits = models.CharField(max_length=60, blank=True, verbose_name="PRODUITS")
    descriptions = models.TextField(max_length=400, verbose_name="DESCRIPTIONS")
    prix = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False, verbose_name="PRIX €")
    date = models.DateField(verbose_name="DATE")
    images = models.ImageField(upload_to='images', verbose_name="PHOTOS")
    promotions = models.ForeignKey('Promo', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = "Articles"

    def __str__(self):
        return f"{self.categories} - {self.produits} - {self.prix}"


class Promo(models.Model):
    produits = models.CharField(max_length=60, blank=True, verbose_name="PRODUITS")
    promo_prix = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="PRIX €")
    promo_date_on = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="DATE DEBUT")
    promo_date_end = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="DATE FIN")
    promo_remise = models.DecimalField(max_digits=8, decimal_places=0, null=True, blank=True,
                                       verbose_name="Promotions %")

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = "Promotions"

    def __str__(self):
        return f"{self.promo_remise} %"


class Categories(models.Model):

    categories = models.CharField(max_length=60, blank=True, verbose_name="CATEGORIE")

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = "Catégories"

    def __str__(self):
        return f"{self.categories}"

