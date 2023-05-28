from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    descriptif = models.TextField()

class Film(models.Model):
    titre = models.CharField(max_length=255)
    annee_sortie = models.IntegerField()
    affiche = models.BinaryField(null=True)  # longblob translates to BinaryField in Django
    realisateur = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)  # foreign key to Categorie

class Acteur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.IntegerField()
    photos = models.BinaryField(null=True)

class Film_Acteur(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)

class Personne(models.Model):
    PROFESSIONNEL = 'professionnel'
    AMATEUR = 'amateur'
    TYPE_CHOICES = [
        (PROFESSIONNEL, 'Professionnel'),
        (AMATEUR, 'Amateur'),
    ]

    pseudo = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)  
    type = models.CharField(max_length=13, choices=TYPE_CHOICES)

class Commentaire(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date = models.DateField()
