from django.shortcuts import render, HttpResponseRedirect
from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request, 'filmographie/index.html')

def add_Categorie(request):
    form = forms.Categorie_Form
    return render(request, 'filmographie/add_form.html', {"form" : form})

#def update_Categorie(request):

#def delete_Categorie(request):

def view_Categorie(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    films = models.Film.objects.filter(categorie=categorie)
    return render(request, 'filmographie/view_categorie.html', {'categorie': categorie, 'films': films})



def view_all_Categorie(request):
    id = "categorie"
    liste = list(models.Categorie.objects.all())
    return render(request, 'filmographie/view_all.html',{'liste':liste, "id":id})

def add_Film(request):
    form = forms.Film_Form
    return render(request, 'filmographie/add_form.html', {'form' : form})

#def update_Film(request):

#def delete_Film(request):

def view_Film(request, id):
    film = models.Film.objects.get(pk=id)
    categorie = film.categorie
    acteurs = models.Film_Acteur.objects.filter(film=film).values('acteur')
    related_actors = models.Acteur.objects.filter(id__in=acteurs)

    return render(request, 'filmographie/view_film.html', {'film':film, 'categorie':categorie, 'acteurs':related_actors})

def view_all_Film(request):
    id = "film"
    liste = list(models.Film.objects.all())
    return render(request, 'filmographie/view_all.html',{'liste':liste, "id":id})


def add_Acteur(request):
    form = forms.Acteur_Form
    return render(request, 'filmographie/add_form.html', {'form': form})

#def update_Acteur(request):

#def delete_Acteur(request):

def view_Acteur(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    films = models.Film_Acteur.objects.filter(acteur=acteur).values('film')
    related_films = models.Film.objects.filter(id__in=films)
    return render(request, 'filmographie/view_acteur.html', {'acteur':acteur, "films":related_films})


def view_all_Acteur(request):
    id = "acteur"
    liste = list(models.Acteur.objects.all())
    return render(request, 'filmographie/view_all.html',{'liste':liste, "id":id})


def add_Personne(request):
    form = forms.Personne_Form
    return render(request, 'filmographie/add_form.html', {"form" : form})

#def update_Personne(request):

#def delete_Personne(request):

#def view_Personne(request):

#def view_all_Personne(request):

def add_Commentaire(request):
    form = forms.Commentaire_Form
    return render(request, 'filmographie/add_form.html', {'form': form, 'test':form})

#def update_Commentaire(request):

#def delete_Commentaire(request):

#def view_Commentaire(request):
   
#def view_all_Commentaire(request):

'''def traitement(request, id):
    if id == 1:
        form = forms.Categorie_Form(request.POST)
    elif id == 2:
        form = forms.Film_Form(request.POST)
    elif id == 3:
        form = forms.Acteur_Form(request.POST)
    #elif id == 4:
        
    elif id == 5 :
        form = forms.Personne_Form(request.POST)
    elif id == 6:
        form = forms.Commentaire_Form(request.POST)
    
    if form.is_valid():# type: ignore
        form.save()# type: ignore
        return HttpResponseRedirect( "/filmographie/submitted/")
    else:
        return render(request, 'filmographie/add_form.html',{'form':form})# type: ignore
  '''

def traitement(request, id):
    form_class_dict = {
        1: forms.Categorie_Form,
        2: forms.Film_Form,
        3: forms.Acteur_Form,
        4: forms.Relation_Form,
        5: forms.Personne_Form,
        6: forms.Commentaire_Form,
    }

    FormClass = form_class_dict.get(id)
    if not FormClass:
        return HttpResponseRedirect('/filmographie/')  # Handle invalid form ID case

    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = FormClass()
    return render(request, 'filmographie/add_form.html', {'form': form})  

def submitted(request):
    return render(request, 'filmographie/submitted.html')


def add_Relation(request):
    form = forms.Relation_Form
    return render(request, 'filmographie/add_form.html', {"form" : form})