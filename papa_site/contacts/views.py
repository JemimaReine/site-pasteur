from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def contacts(request):
    context = {}

    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Enregistrer dans la base de données
        Contact.objects.create(
            nom=nom,
            email=email,
            message=message
        )

        # Envoyer l’e-mail
        sujet = f"Nouveau message de contact de {nom}"
        contenu = f"Nom : {nom}\nEmail : {email}\n\nMessage :\n{message}"
        destinataires = ['reinejemimatrinitekokobe@gmail.com']

        send_mail(
            sujet,
            contenu,
            settings.DEFAULT_FROM_EMAIL,
            destinataires,
            fail_silently=False
        )

        # Indiquer à la template que l’envoi a réussi
        context['message_envoye'] = True
        context['nom'] = nom

    return render(request, 'contacts.html', context)
