from django.shortcuts import render, get_object_or_404
# Create your views here.
#from django.http import HttpResponse
from .models import Tournoi, Poule, Match, Comment
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .forms import CommentForm
#from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.shortcuts import redirect, resolve_url
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

def poules(request,tournoi_id, poule_id):
    poule = get_object_or_404(Poule, pk=poule_id)
    equipes = poule.liste_equipe.all().order_by('non')
    tournoi = get_object_or_404(Tournoi, pk = tournoi_id)
    matchs = poule.match_set.all().order_by('date')
    print(matchs)
    return render(request, 'visualisation/poules.html', {'selected_equipe': equipes,  'numero': poule.numero_poule, 'matchs':matchs, 'tournoi':tournoi})

def match(request,tournoi_id, match_id):
    matchh = get_object_or_404(Match, pk = match_id)
    tournoi = get_object_or_404(Tournoi, pk = tournoi_id)
    #poule = match.poule
    #comment = match.comment_set.all().order_by('created_data')
    comment =[]
    comment_list =Comment.objects.all()
    for commentt in comment_list:
        if commentt.content_type == matchh:
            comment.append(commentt)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.content_type = matchh
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm(None)
    
    return render(request, 'visualisation/Match.html', {'match': matchh, 'comment': comment, 'form': form, 'tournoi':tournoi} )
    #après je vais ajuter des commentair
    
def modifComment(request, tournoi_id, match_id, comment_id):
    matchh = get_object_or_404(Match, pk = match_id)
    commentt = get_object_or_404(Comment, pk = comment_id)
    tournoi = get_object_or_404(Tournoi, pk = tournoi_id)
    
    
    form = CommentForm(request.POST, instance=commentt)
    if request.method == 'POST':
        if commentt.author == request.user:  # se o usuário for o autor do comentário
            form = CommentForm(request.POST, instance=commentt)
            if form.is_valid():
                form.save()
                redirect_url = request.META.get('HTTP_REFERER')
                previous_path = '/'.join(redirect_url.split('/')[:-3])
                destination_url = resolve_url(previous_path)
                return redirect(destination_url)
            else:
                form = CommentForm(None)     
                
        else:
            form = CommentForm(None)    
    else:
            form = CommentForm(None)     
    return render(request, 'visualisation/modifComment.html', {'match': matchh, 'comment': commentt, 'form': form, 'tournoi':tournoi})
    
    
    
    