from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import Sitemap
from django.http import HttpResponse
import os

from .models import Product, OtherModel1, OtherModel2  # Import your models here
from bag.models import YourBagModel  # Import your bag model here
from profiles.models import YourProfileModel  # Import your profile model here

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home']  # Add other static views here

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()  # Update with your actual product queryset

    def lastmod(self, obj):
        return obj.updated_at  # Update with the last modified date of the product

class BagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return YourBagModel.objects.all()  # Update with your queryset for the bag items

    def lastmod(self, obj):
        return obj.updated_at  # Update with the last modified date of bag items

class ProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return YourProfileModel.objects.all()  # Update with your queryset for the profile items

    def lastmod(self, obj):
        return obj.updated_at  # Update with the last modified date of profile items

def sitemap_xml(request):
    # Path to the sitemap.xml file
    sitemap_path = os.path.join(os.path.dirname(__file__), 'sitemap.xml')
    
    # Read the contents of the sitemap.xml file
    with open(sitemap_path, 'rb') as f:
        xml_content = f.read()

    # Return the XML content as HttpResponse
    return HttpResponse(xml_content, content_type='application/xml')

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'bag': BagSitemap,
    'profile': ProfileSitemap,
    # Add more sitemaps for other models or apps if needed
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    
    # Sitemap URL pattern
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
