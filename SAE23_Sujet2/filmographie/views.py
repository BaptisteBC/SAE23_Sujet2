from django.shortcuts import render, HttpResponseRedirect
from . import forms
from . import models
import csv

def index(request):
    return render(request, 'filmographie/index.html')



def note_moy(id):
    film = models.Film.objects.get(pk=id)
    coms = models.Commentaire.objects.filter(film=film)
    total = 0
    count = len(coms)
    
    if count > 0:
        for com in coms:
            total += com.note
        moy = round(total / count, 2)
        return moy
    else:
        return None



def add_Categorie(request):
    form = forms.Categorie_Form
    return render(request, 'filmographie/add_form.html', {"form" : form})

def update_Categorie(request,id):
    categorie = models.Categorie.objects.get(pk=id)
    form = forms.Categorie_Form(categorie.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})

def delete_Categorie(request,id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/filmographie/view_all/categorie/")

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

def update_Film(request,id):
    film = models.Film.objects.get(pk=id)
    form = forms.Film_Form(film.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})

def delete_Film(request,id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/filmographie/view_all/film/")

def view_Film(request, id):
    film = models.Film.objects.get(pk=id)
    categorie = film.categorie
    liste = models.Film_Acteur.objects.filter(film=film).values('acteur')
    acteurs = models.Acteur.objects.filter(id__in=liste)
    coms = models.Commentaire.objects.filter(film=film)
    note = note_moy(id)
    return render(request, 'filmographie/view_film.html', {'film':film, 'categorie':categorie, 'acteurs':acteurs, 'commentaire':coms, 'moyenne':note})

def view_all_Film(request):
    id = "film"
    liste = list(models.Film.objects.all())
    return render(request, 'filmographie/view_all.html',{'liste':liste, "id":id})



def add_Acteur(request):
    form = forms.Acteur_Form
    return render(request, 'filmographie/add_form.html', {'form': form})

def update_Acteur(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    form = forms.Acteur_Form(acteur.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})

def delete_Acteur(request,id):
    acteur = models.Acteur.objects.get(pk=id)
    acteur.delete()
    return HttpResponseRedirect("/filmographie/view_all/acteur/")

def view_Acteur(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    liste = models.Film_Acteur.objects.filter(acteur=acteur).values('film')
    films = models.Film.objects.filter(id__in=liste)
    return render(request, 'filmographie/view_acteur.html', {'acteur':acteur, "films":films})

def view_all_Acteur(request):
    id = "acteur"
    liste = list(models.Acteur.objects.all())
    return render(request, 'filmographie/view_all.html',{'liste':liste, "id":id})



def add_Personne(request):
    form = forms.Personne_Form
    return render(request, 'filmographie/add_form.html', {"form" : form})

def update_Personne(request,id):
    user = models.Personne.objects.get(pk=id)
    form = forms.Personne_Form(user.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})

def delete_Personne(request,id):
    personne = models.Personne.objects.get(pk=id)
    personne.delete()
    return HttpResponseRedirect("/filmographie/")

def view_Personne(request,id):
    personne = models.Personne.objects.get(pk=id)
    coms = models.Commentaire.objects.filter(personne=personne)
    return render(request, 'filmographie/view_user.html', {'user':personne, 'coms':coms})



def add_Commentaire(request):
    form = forms.Commentaire_Form
    return render(request, 'filmographie/add_form.html', {'form': form, 'test':form})

def update_Commentaire(request, id):
    com = models.Commentaire.objects.get(pk=id)
    form = forms.Commentaire_Form(com.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})

def delete_Commentaire(request,id):
    com = models.Commentaire.objects.get(pk=id)
    personne = com.personne.id  # type: ignore
    com.delete()
    return HttpResponseRedirect(f"/filmographie/view/user/{personne}")



def submitted(request):
    return render(request, 'filmographie/submitted.html')



def add_Relation(request):
    form = forms.Relation_Form
    return render(request, 'filmographie/add_form.html', {"form" : form})



def traitement(request, id):
    test_forms = {
        1: forms.Categorie_Form,
        2: forms.Film_Form,
        3: forms.Acteur_Form,
        4: forms.Relation_Form,
        5: forms.Personne_Form,
        6: forms.Commentaire_Form,
    }

    class_form = test_forms.get(id)
    if not class_form:
        return HttpResponseRedirect('/filmographie/')  

    if request.method == 'POST':
        form = class_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = class_form()
    return render(request, 'filmographie/add_form.html', {'form': form})  



def traitement_update(request, id):
    if id == 1:
        form = forms.Categorie_Form(request.POST)
    elif id == 2:
        form = forms.Film_Form(request.POST)
    elif id == 3:
        form = forms.Acteur_Form(request.POST)
    elif id == 4:
        form = forms.Relation_Form(request.POST)
    elif id == 5 :
        form = forms.Personne_Form(request.POST)
    elif id == 6:
        form = forms.Commentaire_Form(request.POST)
    
    if form.is_valid():# type: ignore
        objct = form.save(commit=False)# type: ignore
        objct.id = id
        objct.save()
        return HttpResponseRedirect( "/filmographie/submitted/")
    else:
        return render(request, 'filmographie/update_form.html',{'form':form, 'id':id})# type: ignore





'''
def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if csv_file.name.endswith('.csv'):
            data_reader = csv.reader(csv_file)
            for row in data_reader:
                col1, col2 = row
                # Create a new instance of YourModel and save it to the database
                models.Categorie.objects.create(nom=col1, descriptif=col2)
            return render(request, '/filmographie/submitted.html')
    return render(request, '/filmographie/index.html')'''