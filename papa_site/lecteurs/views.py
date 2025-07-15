from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm
from .models import NewsletterSubscriber

def inscrire_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Merci de vous être inscrit à la newsletter !")
            else:
                messages.info(request, "Cet email est déjà inscrit.")
        else:
            messages.error(request, "Adresse email invalide.")
    return redirect(request.META.get('HTTP_REFERER', '/'))