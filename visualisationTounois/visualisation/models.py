from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




# Create your models here.

class Poule(models.Model):
    numero_poule = models.IntegerField()
    tournoi = models.ForeignKey('Tournoi', on_delete=models.CASCADE)
    liste_equipe = models.ManyToManyField('Equipe')
    def __str__(self) -> str:
        return "Poule" + str(self.numero_poule)
    
   
 
class Equipe(models.Model):
    non = models.CharField(max_length=50)
    non_entraineur = models.CharField(max_length=20)
    #liste_joueurs = models.ManyToManyField("Joueur") 
    def __str__(self):
        return self.non

class Match(models.Model):
    date = models.DateTimeField()
    lieu = models.CharField(max_length=50)
    equipe1 = models.ForeignKey('Equipe', related_name='partidas1',on_delete=models.CASCADE)
    equipe2 = models.ForeignKey('Equipe', related_name='partidas2',on_delete=models.CASCADE)
    score = models.IntegerField()
    poule= models.ForeignKey('Poule', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.equipe1.non + " vs " + self.equipe2.non

    


class Joueur(models.Model):
    non = models.CharField(max_length=20)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE)


    
class Tournoi(models.Model):
    non = models.CharField(max_length=50)
    non_lieu = models.CharField(max_length=50, null=True)
    data_debut = models.DateField(null=True) 
    data_fin =models.DateField(null=True)
    liste_equipes = models.ManyToManyField("Equipe")
    #decouvrir comment faire le numéro aux poulle 
    nombre_de_poules = models.IntegerField()
    def __str__(self):
        return str(self.pk)
    def datas(self):
        return " ".join(self.split()[:3])
    
    
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        super(Comment, self).save(*args, **kwargs)
    
