from django import forms
from .models import Order
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['default_phone_number', 'default_country', 'default_postcode', 'default_town_or_city', 'default_street_address1', 'default_street_address2', 'default_county']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number', 'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country', 'county',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name', 'email': 'Email Address', 'phone_number': 'Phone Number',
            'postcode': 'Postal Code', 'town_or_city': 'Town or City', 'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2', 'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                placeholder = f"{placeholders[field]} {'*' if self.fields[field].required else ''}"
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        # Hide the username field if it's not needed
        if 'username' in self.fields:
            self.fields['username'].widget = forms.HiddenInput()