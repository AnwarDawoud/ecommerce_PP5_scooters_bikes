# In checkout/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Order

class OrderSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Order.objects.all()

    def lastmod(self, obj):
        return obj.created_at
