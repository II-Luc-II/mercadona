import zoneinfo
from datetime import timezone
from io import BytesIO
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from .models import Catalogue, Promo, Categories
from django.http import HttpResponse
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
)


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
        categories = Categories.objects.all()
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
                    produit.prix_affiche = produit.prix
                    produit.promo_active = False
                elif promo.promo_date_on and promo.promo_date_on > current_date:
                    # La promotion n'a pas encore commencé
                    produit.prix_affiche = produit.prix
                    produit.promo_active = False
                else:
                    if promo.promo_remise:
                        remise = promo.promo_remise / 100
                        prix_remise = produit.prix * (1 - remise)
                        produit.prix_affiche = prix_remise
                        produit.promo_active = True
                    else:
                        produit.prix_affiche = produit.prix
                        produit.promo_active = False
            else:
                produit.prix_affiche = produit.prix
                produit.promo_active = False

            produit.save()

        return render(request, 'home.html', context={'categories': categories, 'produits': produits})
    except Catalogue.DoesNotExist:
        raise Http404("Le catalogue n'existe pas.")


def promo_pdf(request):
    # Récupérer les articles en promotion
    produits = Catalogue.objects.filter(promotions__isnull=False)

    # Créer un buffer mémoire pour stocker le PDF
    buffer = BytesIO()

    # Créer le document PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Styles de paragraphe
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    subtitle_style = styles["Heading2"]
    text_style = styles["Normal"]

    # Liste pour les éléments du document
    elements = []

    # Parcourir les articles en promotion et ajouter les détails au PDF
    for produit in produits:
        # Ajouter l'image
        if produit.images:
            image = Image(produit.images.path, width=100, height=100)
            elements.append(image)

        # Ajouter le nom du produit
        produit_name = produit.produits
        elements.append(Paragraph(produit_name, title_style))

        # Ajouter le prix d'origine
        produit_price = f"Prix: €{produit.prix}"
        elements.append(Paragraph(produit_price, text_style))

        # Vérifier s'il y a une promotion
        if produit.promotions:
            promo = produit.promotions

            # Ajouter la remise
            promo_remise = f"Remise: {promo.promo_remise}%"
            elements.append(Paragraph(promo_remise, text_style))

            # Calculer le prix en promotion
            prix_promo = produit.prix - (produit.prix * promo.promo_remise / 100)
            prix_promo_text = f"Prix en promotion: €{prix_promo}"
            elements.append(Paragraph(prix_promo_text, text_style))

            # Ajouter la date de début et de fin de la promotion
            promo_date_on = f"Début de la promotion: {promo.promo_date_on}"
            elements.append(Paragraph(promo_date_on, text_style))

            promo_date_end = f"Fin de la promotion: {promo.promo_date_end}"
            elements.append(Paragraph(promo_date_end, text_style))

        # Ajouter un espace
        elements.append(Spacer(1, 12))

    # Construire le document PDF
    doc.build(elements)

    # Obtenir le contenu du buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    # Créer une réponse HTTP avec le contenu du PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="promotions.pdf"'
    response.write(pdf_data)

    return response