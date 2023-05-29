from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajout_acteur/', views.add_Acteur),
    path('ajout_commentaire/', views.add_Commentaire),
    path('ajout_film/', views.add_Film),
    path('inscription/', views.add_Personne),
    path('ajout_categorie/', views.add_Categorie),
    path('traitement/<int:id>/', views.traitement),
    path('submitted/', views.submitted),
]