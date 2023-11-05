from rest_framework import serializers
from myservice.models import Produit , Adresse , Client , ModePaiement , Commande , LigneCommande , RetourProduit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id', 'nom', 'description', 'prix', 'stock')

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'nom', 'prenom', 'adresse', 'code_postal', 'ville')

class ModePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModePaiement
        fields = ('id', 'nom')

class ClientSerializer(serializers.ModelSerializer):
    adresses = AdresseSerializer(many=True)
    modes_paiement = ModePaiementSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'nom', 'email', 'adresses', 'modes_paiement', 'points_fidelite')

class CommandeSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Commande
        fields = ('id', 'date', 'montant', 'etat', 'client')

class LigneCommandeSerializer(serializers.ModelSerializer):
    commande = CommandeSerializer()
    produit = ProduitSerializer()

    class Meta:
        model = LigneCommande
        fields = ('id', 'commande', 'produit', 'quantite')

class RetourProduitSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer()

    class Meta:
        model = RetourProduit
        fields = ('id', 'produit', 'quantite', 'etat')
