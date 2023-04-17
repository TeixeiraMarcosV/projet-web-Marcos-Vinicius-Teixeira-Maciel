from django.shortcuts import render, get_object_or_404
# Create your views here.
#from django.http import HttpResponse
from .models import Tournoi, Poule
from django.http import Http404
# ...
def index(request):
    try:
        Tournois = Tournoi.objects.order_by('data_debut')
    except Tournoi.DoesNotExist:
        raise Http404("-------------")
    return render(request, 'visualisation/index.html', {'Tournois': Tournois})



def tournoii(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    poules = tournoi.poule_set.all().order_by('numero_poule')
    
    if request.method == 'POST':
        try:
            selected_poule = poules.get(pk=request.POST['poule'])
        except (KeyError, poules.model.DoesNotExist):
            raise Http404("Cette poule n'existe pas.")
        else:
            return render(request, 'visualisation/tournoii.html', {'selected_poule': selected_poule, 'non': tournoi.non})
    
    return render(request, 'visualisation/tournoii.html', {'poules': poules, 'non': tournoi.non})
