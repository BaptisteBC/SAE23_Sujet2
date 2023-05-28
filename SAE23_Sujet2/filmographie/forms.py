from django.forms import ModelForm, ChoiceField
from django.utils.translation import gettext_lazy as _
from . import models

class Categorie_Form(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'descriptif',)
        labels = {
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
        }

class Film_Form(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'annee_sortie',  'realisateur', 'categorie',) # test sans 'affiche',
        labels = {
            'titre': _('Titre'),
            'annee_sortie': _('Année de sortie'),
            #'affiche': _('Affiche'),
            'realisateur': _('Réalisateur'),
            'categorie': _('Categorie'),
        }

class Acteur_Form(ModelForm):
    class Meta:
        model = models.Acteur
        fields = ('nom', 'prenom', 'age', )# test sans 'photos',
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'age': _('Âge'),
            #'photos': _('Photos'),
        }

class FilmActeur_Form(ModelForm):
    class Meta:
        model = models.Film_Acteur
        fields = ('film', 'acteur',)
        labels = {
            'film': _('Film'),
            'acteur': _('Acteur'),
        }

class Personne_Form(ModelForm):
    type = ChoiceField(
        choices=[('', 'Choisir')] + list(models.Personne.TYPE_CHOICES),
        label=_('Type'),
        error_messages={
        'required': _('Vous devez choisir un type'),
    }
    )
    class Meta:
        model = models.Personne
        fields = ('pseudo', 'nom', 'prenom', 'mail', 'mot_de_passe', 'type',)
        labels = {
            'pseudo': _('Pseudo'),
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'mail': _('Mail'),
            'mot_de_passe': _('Mot de passe'),
            'type': _('Type'),
        }

class Commentaire_Form(ModelForm):
    class Meta:
        model = models.Commentaire
        fields = ('film', 'personne', 'note', 'commentaire', 'date',)
        labels = {
            'film': _('Film'),
            'personne': _('Personne'),
            'note': _('Note'),
            'commentaire': _('Commentaire'),
            'date': _('Date'),
        }
        localized_fields = ('date',)
