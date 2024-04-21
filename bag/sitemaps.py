from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BagItem  # Import the BagItem model from the correct location

class BagSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return BagItem.objects.all()

    def location(self, obj):
        return reverse('bag:bag_detail', args=[obj.id])  # Adjust the reverse URL name as per your project
