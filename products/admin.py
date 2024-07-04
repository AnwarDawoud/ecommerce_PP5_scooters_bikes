from django.contrib import admin
from .models import Category, Product, Review, Wishlist


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

# Register the Review model with the admin site
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'date_added')
    list_filter = ('product', 'rating', 'date_added')
    search_fields = ('product__name', 'user__username', 'comment')
    date_hierarchy = 'date_added'
    ordering = ('-date_added',)
    
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_date')
    list_filter = ('user', 'added_date')
    search_fields = ('user__username', 'product__name')
    
