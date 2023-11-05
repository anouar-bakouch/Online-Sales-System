from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client , Produit , Commande , ModePaiement , LigneCommande , Adresse , RetourProduit
from .serializers import ClientSerializer , ProduitSerializer , ModePaiementSerializer , LigneCommandeSerializer , AdresseSerializer , RetourProduitSerializer


def index(request):

    return render(request,'index.html')

# Client 
class ClientAPIView(APIView):
    """
    API view for the `Client` model.
    """

    def get(self, request):
        """
        Get all clients.
        """
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new client.
        """
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing client.
        """
        client = Client.objects.get(pk=pk)
        client.delete()
        return Response(status=204)

# Produit 
class ProduitAPIView(APIView):
    """
    API view for the `Produit` model.
    """
    def get(self, request):
        """
        Get all products.
        """
        products = Produit.objects.all()
        serializer = ProduitSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new product.
        """
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing product.
        """
        product = Produit.objects.get(pk=pk)
        product.delete()
        return Response(status=204)

# Commande 
class CommandeAPIView(APIView):
    """
    API view for the `Commande` model.
    """

    def get(self, request):
        """
        Get all commandes.
        """
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new commande.
        """
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing commande.
        """
        commande = Commande.objects.get(pk=pk)
        commande.delete()
        return Response(status=204)

# Adresse
class AdresseAPIView(APIView):
    """
    API view for the `Adresse` model.
    """

    def get(self, request):
        """
        Get all addresses.
        """
        adresses = Adresse.objects.all()
        serializer = AdresseSerializer(adresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new address.
        """
        serializer = AdresseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing address.
        """
        adresse = Adresse.objects.get(pk=pk)
        adresse.delete()
        return Response(status=204)

# Mode Paiement 
class ModePaiementAPIView(APIView):
    """
    API view for the `ModePaiement` model.
    """

    def get(self, request):
        """
        Get all payment methods.
        """
        modes_paiement = ModePaiement.objects.all()
        serializer = ModePaiementSerializer(modes_paiement, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new payment method.
        """
        serializer = ModePaiementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing payment method.
        """
        mode_paiement = ModePaiement.objects.get(pk=pk)
        mode_paiement.delete()
        return Response(status=204)

# Ligne Commande
class LigneCommandeAPIView(APIView):
    """
    API view for the `LigneCommande` model.
    """

    def get(self, request):
        """
        Get all order lines.
        """
        lignes_commande = LigneCommande.objects.all()
        serializer = LigneCommandeSerializer(lignes_commande, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new order line.
        """
        serializer = LigneCommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing order line.
        """
        ligne_commande = LigneCommande.objects.get(pk=pk)
        ligne_commande.delete()
        return Response(status=204)

# Retour RetourProduit
class RetourProduitAPIView(APIView):
    """
    API view for the `RetourProduit` model.
    """

    def get(self, request):
        """
        Get all product returns.
        """
        retour_produits = RetourProduit.objects.all()
        serializer = RetourProduitSerializer(retour_produits, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new product return.
        """
        serializer = RetourProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        Delete an existing product return.
        """
        retour_produit = RetourProduit.objects.get(pk=pk)
        retour_produit.delete()
        return Response(status=204)