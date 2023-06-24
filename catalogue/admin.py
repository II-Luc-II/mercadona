from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Catalogue, Promo, Categories
from django.urls import reverse
from django.utils.safestring import mark_safe


admin.site.unregister(Group)
admin.site.site_header = 'Administration Mercadona'


@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
    list_display = ('categories', 'produits', 'promotions', 'prix')
    list_display_links = ('promotions', )
    list_filter = ('categories', )
    empty_value_display = "-Cliquer pour ajouter-"


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('produits', 'promo_prix', 'promo_date_on', 'promo_date_end', 'promo_remise', 'promo_pdf_link')
    exclude = ('promo_prix',)

    def promo_pdf_link(self, obj):
        pdf_url = reverse('promo_pdf')  # Nom de l'URL correspondant à la vue qui va générer le PDF
        return mark_safe(f'<a href="{pdf_url}">Télécharger en PDF</a>')

    promo_pdf_link.short_description = 'PDF'  # Texte à afficher dans l'en-tête de colonne


@admin.register(Categories)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('categories', )

# Register your models here.
