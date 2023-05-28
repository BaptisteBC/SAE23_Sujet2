from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'filmographie/index.html')

def Commentaire(request):
    return render(request, 'filmographie/Commentaire.html')

def SignIn(request):
    return render(request, 'filmographie/SignIn.html')