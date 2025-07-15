from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from .models import Livre, Commande
from home.models import Pasteur

def books(request):
    livres_list = Livre.objects.all().order_by('-id')  # Plus récent d'abord
    pasteur = Pasteur.objects.first()
    paginator = Paginator(livres_list, 3)  # 6 livres par page
    page = request.GET.get('page')
    livres = paginator.get_page(page)

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        quantite = request.POST.get('quantite')
        livre_id = request.POST.get('livre_id')

        if not all([nom, prenom, telephone, email, quantite, livre_id]):
            return JsonResponse({'success': False, 'message': "Veuillez remplir tous les champs."})

        try:
            livre = Livre.objects.get(id=livre_id)
            Commande.objects.create(
                nom=nom,
                prenoms=prenom,
                telephone=telephone,
                email=email,
                livre=livre,
                quantite=quantite
            )

            send_mail(
                subject="Confirmation de votre commande",
                message=f"Bonjour {prenom}, votre commande pour le livre '{livre.titre}' (x{quantite}) a bien été reçue.",
                from_email="ton@email.com",
                recipient_list=[email],
                fail_silently=True
            )

            return JsonResponse({'success': True, 'message': "Commande envoyée avec succès."})
        except Exception as e:
            print("Erreur :", e)
            return JsonResponse({'success': False, 'message': "Erreur serveur."})

    return render(request, 'books.html', {'livres': livres,   'pasteur': pasteur,})
