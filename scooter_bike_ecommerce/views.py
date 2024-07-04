"""
Views for handling various HTTP requests in the scooter_bike_ecommerce application.

This module contains view functions for rendering error pages and generating
robots.txt content for the scooter_bike_ecommerce Django application.
"""

from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception):
    """ Custom handler for 404 errors """
    return render(request, 'errors/404.html', status=404)


def robots_txt():
    """
    View function for generating robots.txt content.

    Generates a robots.txt file with rules for web crawlers, including
    allowing access to specific URLs like /, /products/, and /categories/,
    and specifying the location of the sitemap.
    
    Parameters:
    - request: HttpRequest object representing the incoming request.

    Returns:
    - HttpResponse object containing the generated robots.txt content.
    """
    lines = [
        "User-agent: *",
        "",
        "# Allow everything",
        "Disallow:",
        "",
        "# Allow specific URLs or directories explicitly",
        "Allow: /$",
        "Allow: /products/",
        "Allow: /categories/",
        "",
        "# Sitemap location",
        "Sitemap: https://scooter-bike-ecommerce-pp5-fa03149f5b15.herokuapp.com/"
                  "templates/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
