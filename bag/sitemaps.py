# In bag/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import BagItem

class BagItemSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return BagItem.objects.all()

    def lastmod(self, obj):
        return obj.last_updated
