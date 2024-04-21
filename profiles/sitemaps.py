# In profiles/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import UserProfile

class UserProfileSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return UserProfile.objects.all()

    def lastmod(self, obj):
        return obj.last_updated
