"""
URL configuration for the scooter_bike_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from products.sitemaps import ProductSitemap
from bag.sitemaps import BagSitemap
from profiles.sitemaps import UserProfileSitemap
from . import views
from .views import robots_txt
from django.contrib.auth import views as auth_views


sitemaps = {
    'products': ProductSitemap,
    'bag': BagSitemap,
    'profile': UserProfileSitemap,

    # Add more sitemaps for other models or apps if needed
}

def sitemap_xml(request):
    """
    Generate the sitemap XML.

    This function handles the request to generate the sitemap XML
    for the website.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the sitemap XML.
    """
    return sitemap_views.sitemap(request, sitemaps)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    # Sitemap URL pattern
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
    # Robots.txt URL pattern
    path('robots.txt', robots_txt, name='robots_txt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.handler404
