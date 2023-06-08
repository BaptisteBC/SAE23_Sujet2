from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajout/categorie/', views.add_Categorie),
    path('ajout/film/', views.add_Film),
    path('ajout/acteur/', views.add_Acteur),
    path('ajout/inscription/', views.add_Personne),
    path('ajout/commentaire/', views.add_Commentaire),
    path('ajout/relation/', views.add_Relation),
    path('traitement/<int:id>/', views.traitement),
    path('submitted/', views.submitted),
    path('view_all/categorie/', views.view_all_Categorie),
    path('view_all/film/', views.view_all_Film),
    path('view_all/acteur/', views.view_all_Acteur),
    path('view/film/<int:id>/', views.view_Film),
    path('view/categorie/<int:id>/', views.view_Categorie),
    path('view/acteur/<int:id>/', views.view_Acteur),
    path('view/user/<int:id>/',views.view_Personne),
    path('delete/categorie/<int:id>/',views.delete_Categorie),
    path('delete/film/<int:id>/',views.delete_Film),
    path('delete/acteur/<int:id>/', views.delete_Acteur),
    path('delete/user/<int:id>/',views.delete_Personne),
    path('delete/commentaire/<int:id>/',views.delete_Commentaire),
    path('update/categorie/<int:id>/', views.update_Categorie),
    path('update/film/<int:id>/', views.update_Film),
    path('update/acteur/<int:id>/', views.update_Acteur),
    path('update/user/<int:id>/', views.update_Personne),
    path('update/commentaire/<int:id>/', views.update_Commentaire),
    path('traitement_update/<int:id>/',views.traitement_update),
    #path('upload/', views.upload_csv, name='upload_csv'),

]