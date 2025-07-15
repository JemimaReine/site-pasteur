from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Citation


def citations(request):
    aujourd_hui = timezone.now().date()
    citation_du_jour = Citation.objects.filter(date=aujourd_hui).first()
    citations_precedentes = Citation.objects.exclude(date=aujourd_hui).order_by('-date')[:4]
   


    query = request.GET.get('q')
    citations = Citation.objects.order_by('-date')
    if query:
        citations = citations.filter(
            Q(titre__icontains=query) |
            Q(contenu__icontains=query)
        )

    paginator = Paginator(citations, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'citations.html', {
        'citation_du_jour': citation_du_jour,
        'citations_precedentes': citations_precedentes,
        'page_obj': page_obj,
        'query': query,
      

    })

def citation_detail(request, pk):
    citation = get_object_or_404(Citation, pk=pk)
    return render(request, 'detail.html', {'citation': citation})
