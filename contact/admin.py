from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email')
