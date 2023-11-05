from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client , Produit , Commande , ModePaiement , LigneCommande , Adresse , RetourProduit
from .serializers import ClientSerializer , ProduitSerializer , ModePaiementSerializer , LigneCommandeSerializer , AdresseSerializer , RetourProduitSerializer


def index(request):

    return render(request,'index.html')

# Client 


# Produit 


# Commande 


# Retour Produit 