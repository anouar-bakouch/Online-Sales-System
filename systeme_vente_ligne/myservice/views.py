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

# Retour Produit 