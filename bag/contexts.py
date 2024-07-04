from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    delivery = Decimal('0.00')
    free_delivery_delta = Decimal('0.00')
    grand_total = Decimal('0.00')
    
    bag = request.session.get('bag', {})
    
    for item_id, quantity in bag.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        except (ValueError, Product.DoesNotExist):
            # Handle the case where item_id is not a valid product ID
            # Log the error or handle it gracefully
            pass
    
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    
    grand_total = total + delivery
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    
    return context
