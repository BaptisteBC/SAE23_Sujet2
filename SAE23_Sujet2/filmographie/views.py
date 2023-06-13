from django.shortcuts import render, HttpResponseRedirect
from . import forms
from . import models
import csv
from io import TextIOWrapper
#from django.http import FileResponse


def import_films_csv(csv_file):
    reader = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'))
    next(reader)
    for row in reader:
        titre_film = row[0]
        annee_sortie = row[1]
        realisateur = row[2]
        categorie = row[3]
        nom_prenom_acteur = row[4:]
        categorie, _ = models.Categorie.objects.get_or_create(nom=categorie)
        film, _= models.Film.objects.get_or_create(titre=titre_film, annee_sortie=annee_sortie, realisateur=realisateur, categorie=categorie)            

        for i in nom_prenom_acteur:
            x = i.split("/")
            nom_acteur = x[0]
            if len(x)>1:
                prenom_acteur = x[1]
            
            acteur, _ = models.Acteur.objects.get_or_create(nom=nom_acteur, prenom=prenom_acteur)  # type: ignore
            models.Film_Acteur.objects.create(film=film, acteur=acteur)

def index(request):
    return render(request, 'filmographie/index.html')

def submitted(request):
    return render(request, 'filmographie/submitted.html')


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


#Consernant les Catégorie

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

#Consernant les films

def add_Film(request):
    form = forms.Film_Form
    return render(request, 'filmographie/add_form.html', {'form' : form})

'''def update_Film(request,id):
    film = models.Film.objects.get(pk=id)
    form = forms.Film_Form(film.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})
'''
def update_Film(request, id):
    film = models.Film.objects.get(pk=id)
    form = forms.Film_Form(instance=film)  # Pass the film instance directly
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})

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
    meilleur_note = models.Commentaire.objects.filter(film=film).order_by('-note')[:1]
    pire_note = models.Commentaire.objects.filter(film=film).order_by('note')[:1]
    note = note_moy(id)
    return render(request, 'filmographie/view_film.html', {'film':film, 'categorie':categorie, 'acteurs':acteurs, 'best':meilleur_note, 'pire':pire_note, 'commentaire':coms, 'moyenne':note})

def view_all_Film(request):
    id = "film"
    liste = list(models.Film.objects.all())
    return render(request, 'filmographie/view_all.html',{'liste':liste, "id":id})



#Consernant les acteurs

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


#Consernant les personnes

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



#Consernant les Commentaires


def add_Commentaire(request):
    film_id = request.GET.get('film_id')
    initial_data = {'film': film_id} if film_id else None
    form = forms.Commentaire_Form(initial=initial_data)
    return render(request, 'filmographie/add_form.html', {'form': form,'test':form})
'''
def update_Commentaire(request, id):
    com = models.Commentaire.objects.get(pk=id)
    form = forms.Commentaire_Form(com.__dict__)
    return render(request, 'filmographie/update_form.html',{"form":form, "id": id})
'''
def update_Commentaire(request, id):
    com = models.Commentaire.objects.get(pk=id)
    form = forms.Commentaire_Form(instance=com)  # Pass the film instance directly
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})


def delete_Commentaire(request,id):
    com = models.Commentaire.objects.get(pk=id)
    personne = com.personne.id  # type: ignore
    com.delete()
    return HttpResponseRedirect(f"/filmographie/view/user/{personne}")




#Consernant les relation films acteurs

def add_Relation(request):
    acteur_id = request.GET.get('acteur_id')
    film_id = request.GET.get('film_id')
    if acteur_id:
        initial_data = {'acteur': acteur_id} 
    elif film_id:
        initial_data = {'film': film_id} 
    else:
        initial_data = None
    form = forms.Relation_Form(initial=initial_data)
    return render(request, 'filmographie/add_form.html', {'form': form})




#Consernant le traitement des ajout et des updates


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




    

def add_Film_csv(request):
    form = forms.ImportFilmCsv
    return render(request, 'filmographie/import_csv.html', {"form" : form})

def import_films(request):
    if request.method == 'POST':
        form = forms.ImportFilmCsv(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            import_films_csv(csv_file)
            return render(request, 'filmographie/submitted.html')
    else:
        form = forms.ImportFilmCsv()
    
    return render(request, 'filmographie/import_csv.html', {'form': form})


def traitement_up_Cat(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.Categorie_Form(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = forms.Categorie_Form(instance=categorie)
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})

def traitement_up_Film(request, id):
    film = models.Film.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.Film_Form(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = forms.Film_Form(instance=film)
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})

def traitement_up_Act(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.Acteur_Form(request.POST, request.FILES, instance=acteur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = forms.Acteur_Form(instance=acteur)
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})

def traitement_up_Pers(request, id):
    pesonne = models.Personne.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.Personne_Form(request.POST, instance=pesonne)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = forms.Personne_Form(instance=pesonne)
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})

def traitement_up_Com(request, id):
    com = models.Commentaire.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.Commentaire_Form(request.POST, instance=com)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = forms.Commentaire_Form(instance=com)
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})

def traitement_up_Rel(request, id):
    rel = models.Film_Acteur.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.Relation_Form(request.POST, instance=rel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/filmographie/submitted/')
    else:
        form = forms.Relation_Form(instance=rel)
    return render(request, 'filmographie/update_form.html', {"form": form, "id": id})