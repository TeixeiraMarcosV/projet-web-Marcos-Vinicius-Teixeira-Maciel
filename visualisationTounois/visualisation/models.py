from django.db import models



# Create your models here.

class Poule(models.Model):
    numero_poule = models.IntegerField()
    tournoi = models.ForeignKey('Tournoi', on_delete=models.CASCADE)
    liste_equipe = models.ManyToManyField('Equipe')
 
class Equipe(models.Model):
    non = models.CharField(max_length=50)
    non_entraineur = models.ForeignKey('Entraineur', on_delete=models.CASCADE)
    liste_joueurs = models.ManyToManyField("Joueur") 
    
class Match(models.Model):
    date = models.DateTimeField()
    lieu = models.CharField(max_length=50)
    equipe1 = models.ForeignKey('Equipe', related_name='partidas1',on_delete=models.CASCADE)
    equipe2 = models.ForeignKey('Equipe', related_name='partidas2',on_delete=models.CASCADE)
    score = models.IntegerField()
    poule= models.ForeignKey('Poule', on_delete=models.CASCADE)
    


class Joueur(models.Model):
    non = models.CharField(max_length=20)

class Entraineur(models.Model):
    nom = models.CharField(max_length=20)
    
class Tournoi(models.Model):
    non = models.CharField(max_length=50)
    non_lieu = models.CharField(max_length=50, null=True)
    data_debut = models.DateField(null=True) 
    data_fin =models.DateField(null=True)
    liste_equipes = models.ManyToManyField("Equipe")
    #decouvrir comment faire le numéro aux poulle 