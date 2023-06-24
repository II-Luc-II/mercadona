from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from catalogue.views import catalogue_list, index, promo_pdf


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('promo_pdf/', promo_pdf, name='promo_pdf'),
    path('home/', catalogue_list, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
