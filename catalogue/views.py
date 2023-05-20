import zoneinfo
from datetime import timezone

from django.http import Http404
from django.shortcuts import render
from django.template.defaultfilters import floatformat
from django.utils import timezone

from catalogue.models import Catalogue, Promo


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)


def index(request):
    try:
        num_promo = Promo.objects.filter(promo_remise__isnull=False).count()

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'index.html', context={'num_promo': num_promo})
    except Promo.DoesNotExist:
        raise Http404("Les promotions n'existent pas.")


def catalogue_list(request):
    try:
        categories = Catalogue.objects.order_by().values_list('categories__categories', flat=True).distinct()
        produits = Catalogue.objects.select_related('promotions').all()

        if 'categories' in request.GET:
            produits = produits.filter(categories__categories=request.GET['categories'])

        current_date = timezone.now()
        for produit in produits:
            if produit.promotions:
                promo = produit.promotions
                if promo.promo_date_end and promo.promo_date_end < current_date:
                    # Supprimer la remise expirée
                    produit.promotions = None
                    produit.prix_affiche = floatformat(produit.prix, 2)
                else:
                    if promo.promo_remise:
                        remise = promo.promo_remise / 100
                        prix_remise = produit.prix * (1 - remise)
                        produit.prix_affiche = floatformat(prix_remise, 2)
                    else:
                        produit.prix_affiche = floatformat(produit.prix, 2)
            else:
                produit.prix_affiche = floatformat(produit.prix, 2)

        return render(request, 'home.html', context={'categories': categories, 'produits': produits})
    except Catalogue.DoesNotExist:
        raise Http404("Le catalogue n'existe pas.")


