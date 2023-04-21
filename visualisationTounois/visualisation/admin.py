from django.contrib import admin
from .models import Tournoi, Equipe, Joueur, Match, Poule, Comment


## Register your models here.
#class TournoiAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['non']}),
    #    (None,               {'fields': ['non_lieu']}),
    #    ('Date information', {'fields': ['data_debut']}),
    #    (None,               {'fields': ['data_fin']}),
    #    ('Equipes', {'fields': ['liste_equipes']}),
    #    ('Nombre de Poules',               {'fields': ['nombre_de_poules']}),
    #]
    #list_display = ('non', 'non_lieu') 

admin.site.register(Tournoi)#, TournoiAdmin)


class JoueurInline(admin.TabularInline):
    model = Joueur
    extra = 10


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('non', 'non_entraineur') 
    inlines = [JoueurInline]
    
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Comment)



#class JoueurInline(admin.TabularInline):
#    model = Joueur
#    extra = 11



        
#class EquipeAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['non']}),
#        ('Entraineur', {'fields': ['non_entraineur']}),
#        ('Entraineur', {'fields': ['non_entraineur']}),
#    ]
#    list_display = ('non', 'non_entraineur')
#    inlines = [JoueurInline]
#    list_filter = ['non']
#    search_fields = ['non']
    
#admin.site.register(Match)#, EquipeAdmin)

#class MatchInline(admin.TabularInline):
   # model = Match
   # extra = 4 

#class PouleAdmin(admin.ModelAdmin): 
    #inlines = [MatchInline]

admin.site.register(Poule) #, PouleAdmin)
admin.site.register(Match)
