from django.test import TestCase

from time import timezone

from django.test import TestCase
from datetime import datetime

from catalogue.models import Catalogue, Promo, Categories


class CatalogueTestCase(TestCase):

    DUMMY_CATALOGUE_PRODUITS = 'TestElement'
    DUMMY_CATEGORIES_CATEGORIES = 'TestElement'

    def setUp(self):

        self.promo = Promo()
        self.promo.name = 'Test Promo List'
        self.promo.save()

        self.promoTestElement = Promo()
        self.promoTestElement.promo_prix = 1200
        self.promoTestElement.promo_date_on = datetime.today()
        self.promoTestElement.promo_date_end = datetime.today()
        self.promoTestElement.promo_remise = 50
        self.promoTestElement.save()

        self.categories = Categories()
        self.categories.categories = 'Test Categories List'
        self.categories.save()

        self.categoriesTestElement = Categories()
        self.categoriesTestElement.categories= self.DUMMY_CATEGORIES_CATEGORIES
        self.categoriesTestElement.save()

    def test_create_catalogue(self):

        nbr_of_catalogues_before_add = Catalogue.objects.count()

        new_catalogue = Catalogue()
        new_catalogue.produits = 'Kimono'
        new_catalogue.descriptions = 'kimono de judo'
        new_catalogue.prix = 250
        new_catalogue.date = datetime.today()
        new_catalogue.images = "media/images/IMG_8696.JPG"
        new_catalogue.promotions = self.promo
        new_catalogue.promo = self.promo
        new_catalogue.categories = self.categories

        new_catalogue.save()

        nbr_of_catalogues_after_add = Catalogue.objects.count()

        self.assertTrue(nbr_of_catalogues_after_add == nbr_of_catalogues_before_add + 1)




