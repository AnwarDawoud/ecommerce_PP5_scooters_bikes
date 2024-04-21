from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from .sitemaps import StaticViewSitemap, ProductSitemap, BagSitemap, ProfileSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'bag': BagSitemap,
    'profile': ProfileSitemap,
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
