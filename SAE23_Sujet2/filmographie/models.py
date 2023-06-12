from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Categorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    descriptif = models.TextField(null = True, blank= True)
    
    def __str__(self):
        return self.nom
    

class Film(models.Model):
    titre = models.CharField(max_length=255, unique=True)
    annee_sortie = models.IntegerField()
    affiche = models.ImageField(upload_to='filmographie/film/', null=True, blank=True)  #NE PAS OUBLIER D'AJOUTER LE TRUC A LA FIN DE SETTINGS, AUSSI DANS URLS.PY et SURTOUT le truc DANS LE HTML
    realisateur = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)  # "foreign key " vers categorie sans le 'to_field'
    
    def __str__(self):
        return self.titre
    

class Acteur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null= True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    photos = models.ImageField(upload_to='filmographie/acteur/', null=True)
    
    def __str__(self):
        return self.nom
    

class Film_Acteur(models.Model):
    film = models.ForeignKey(Film,  on_delete=models.CASCADE)
    acteur = models.ForeignKey(Acteur,  on_delete=models.CASCADE)

class Personne(models.Model):
    PROFESSIONNEL = 'professionnel'
    AMATEUR = 'amateur'
    TYPE_CHOICES = [
        (PROFESSIONNEL, 'Professionnel'),
        (AMATEUR, 'Amateur'),
    ]

    pseudo = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)  
    type = models.CharField(max_length=13, choices=TYPE_CHOICES)

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    note = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
     )
    commentaire = models.TextField()
    date = models.DateField(default=timezone.now().date())  