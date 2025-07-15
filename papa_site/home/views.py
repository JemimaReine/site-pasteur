from django.shortcuts import render
from .models import Pasteur, PenseeDuJour, CarouselImage
from citations.models import Citation
from django.utils import timezone

def home(request):
    pasteur = Pasteur.objects.first()
    aujourd_hui = timezone.now().date()
    citation_du_jour = Citation.objects.filter(date=aujourd_hui).first()
    pensee = PenseeDuJour.objects.order_by('-date').first()
    images = CarouselImage.objects.all()
    return render(request, 'home.html', {
        'images': images,
        'pasteur': pasteur,
        'pensee': pensee,
        'citation_du_jour':citation_du_jour

    })

# Create your views here.
