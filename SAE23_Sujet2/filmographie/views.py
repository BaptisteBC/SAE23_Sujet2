from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request, 'filmographie/index.html')

def add_Categorie(request):
    form = forms.Categorie_Form
    return render(request, 'filmographie/add_Categorie', {"form" : form})

#def update_Categorie(request):

#def delete_Categorie(request):

#def view_Categorie(request):

#def view_all_Categorie(request):

def add_Film(request):
    form = forms.Film_Form
    return render(request, 'filmographie/add_Film', {'form' : form})

#def update_Film(request):

#def delete_Film(request):

#def view_Film(request):

#def view_all_Film(request):

def add_Acteur(request):
    form = forms.Acteur_Form
    return render(request, 'filmographie/add_Acteur', {'form': form})

#def update_Acteur(request):

#def delete_Acteur(request):

#def view_Acteur(request):

#def view_all_Acteur(request):

def add_Personne(request):
    form = forms.Personne_Form
    return render(request, 'filmographie/add_Personne.html', {"form" : form})

#def update_Personne(request):

#def delete_Personne(request):

#def view_Personne(request):

#def view_all_Personne(request):

def add_Commentaire(request):
    form = forms.Commentaire_Form
    return render(request, 'filmographie/post_Commentaire', {'form': form})

#def update_Commentaire(request):

#def delete_Commentaire(request):

'''def view_Commentaire(request):
    return render(request, 'filmographie/Commentaire.html')
'''
#def view_all_Commentaire(request):
