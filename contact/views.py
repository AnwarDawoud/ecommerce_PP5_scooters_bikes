from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactUsForm
from django.core.mail import send_mail
from django.conf import settings

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'New message from your website'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nSubject: {form.cleaned_data["subject"]}\nMessage: {form.cleaned_data["message"]}'
            sender_email = form.cleaned_data['email']
            recipient_list = [settings.EMAIL_HOST_USER] 
            send_mail(subject, message, sender_email, recipient_list)

            # No messages.success() call here

            return HttpResponseRedirect(reverse('contact_us') + '?submitted=True')
    
    else:
        form = ContactUsForm()

    template = 'contact/contactus.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
