from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from products.sitemaps import ProductSitemap
from bag.sitemaps import BagSitemap
from profiles.sitemaps import UserProfileSitemap
from .views import handler404
from .views import robots_txt


sitemaps = {
    'products': ProductSitemap,
    'bag': BagSitemap,
    'profile': UserProfileSitemap,

    # Add more sitemaps for other models or apps if needed
}

def sitemap_xml(request):
    return sitemap_views.sitemap(request, sitemaps)

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
    
    # Robots.txt URL pattern
    path('robots.txt', robots_txt, name='robots_txt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'scooter_bike_ecommerce.views.handler404'
