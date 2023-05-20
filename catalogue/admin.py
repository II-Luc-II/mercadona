from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Catalogue, Promo, Categories

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
    list_display = ('promo_remise', 'promo_date_on', 'promo_date_end',)
    exclude = ('promo_prix', )


@admin.register(Categories)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('categories', )


