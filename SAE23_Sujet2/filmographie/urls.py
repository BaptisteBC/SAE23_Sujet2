from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajout/categorie/', views.add_Categorie),
    path('ajout/film/', views.add_Film),
    path('ajout/acteur/', views.add_Acteur),
    path('ajout/inscription/', views.add_Personne),
    path('ajout/commentaire/', views.add_Commentaire),
    path('traitement/<int:id>/', views.traitement),
    path('submitted/', views.submitted),
    path('view_all/categorie/', views.view_all_Categorie),
    path('view_all/film/', views.view_all_Film),
    path('view_all/acteur/', views.view_all_Acteur),
    path('view/film/<int:id>/', views.view_Film)

]