from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /checkout/",
        "Disallow: /bag/",
        "Disallow: /accounts/",
        "Disallow: /profiles/",
        "Disallow: /login/",
        "Disallow: /register/",
        "",
        "# Allow specific URLs or directories",
        "Allow: /$",
        "Allow: /products/",
        "Allow: /categories/",
        "",
        "# Allow social media profiles",
        "Allow: https://www.facebook.com/profile.php?id=61558736970397",
        "Allow: https://twitter.com/",
        "Allow: https://www.instagram.com/",
        "Allow: https://www.youtube.com/",
        "",
        "Sitemap: https://scooter-bike-ecommerce-pp5-fa03149f5b15.herokuapp.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")