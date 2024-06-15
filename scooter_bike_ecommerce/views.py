from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def robots_txt(request):
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
        "Sitemap: https://scooter-bike-ecommerce-pp5-fa03149f5b15.herokuapp.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")