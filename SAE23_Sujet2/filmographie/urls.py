from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Commentaire/', views.Commentaire),
    path('SignIn/', views.SignIn),
]