from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from .forms import OrderForm, UserProfileForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from bag.contexts import bag_contents
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_POST
def cache_checkout_data(request):
    try:
        client_secret = request.POST.get('client_secret', '')
        if not client_secret:
            raise ValueError("Client secret not provided")

        pid = client_secret.split('_secret')[0]
        metadata = {
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
        }

        if request.user.is_authenticated:
            metadata['username'] = request.user.username

        stripe.PaymentIntent.modify(pid, metadata=metadata)

        return HttpResponse(status=200)
    except stripe.error.StripeError as e:
        error_msg = 'Stripe error: Unable to modify PaymentIntent.'
        messages.error(request, error_msg)
        return HttpResponseServerError(content=error_msg, status=500)
    except Exception as e:
        error_msg = 'Sorry, your payment cannot be processed right now. Please try again later.'
        messages.error(request, error_msg)
        return HttpResponseServerError(content=error_msg, status=500)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST.get('street_address2', ''),
            'county': request.POST.get('county', ''),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.grand_total = bag_contents(request)['grand_total']
            
            if request.user.is_authenticated:
                order.user_profile = request.user.userprofile
            else:
                messages.error(request, 'You need to log in to complete your order.')
                return redirect(reverse('account_login'))

            order.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your bag wasn't found in our database. Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    try:
        order = get_object_or_404(Order, order_number=order_number)

        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = None

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order.user_profile = profile
                order.save()

                save_info = request.session.get('save_info')
                if save_info:
                    profile_data = {
                        'default_phone_number': order.phone_number,
                        'default_country': order.country,
                        'default_postcode': order.postcode,
                        'default_town_or_city': order.town_or_city,
                        'default_street_address1': order.street_address1,
                        'default_street_address2': order.street_address2,
                        'default_county': order.county,
                    }
                    user_profile_form = UserProfileForm(profile_data, instance=profile)
                    if user_profile_form.is_valid():
                        user_profile_form.save()
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found. Your profile information was not updated.')
            except Exception as e:
                messages.error(request, f'Error saving user profile for order {order_number}: {e}')

        messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

        if 'bag' in request.session:
            del request.session['bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'username': username,
        }
        return render(request, template, context)
    except Exception as e:
        messages.error(request, f'Error processing checkout success for order {order_number}: {e}')
        return render(request, '500.html', status=500)
