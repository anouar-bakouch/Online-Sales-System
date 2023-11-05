from rest_framework import serializers
from myservice.models import Produit, Adresse, Client, ModePaiement, Commande, LigneCommande, RetourProduit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id', 'nom', 'description', 'prix', 'stock')

    def create(self, validated_data):
        product = Produit.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ('id', 'adresse', 'code_postal', 'ville')

    def create(self, validated_data):
        address = Adresse.objects.create(**validated_data)
        return address

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class ModePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModePaiement
        fields = ('id', 'nom')

    def create(self, validated_data):
        payment_method = ModePaiement.objects.create(**validated_data)
        return payment_method

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class ClientSerializer(serializers.ModelSerializer):
    adresses = AdresseSerializer(many=True)
    modes_paiement = ModePaiementSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'nom', 'email', 'adresses', 'modes_paiement', 'points_fidelite')

    def create(self, validated_data):
        addresses = validated_data.pop('adresses')
        payment_methods = validated_data.pop('modes_paiement')

        client = Client.objects.create(**validated_data)

        for address in addresses:
            address = Adresse.objects.create(**address)
            client.adresses.add(address)

        for payment_method in payment_methods:
            payment_method = ModePaiement.objects.create(**payment_method)
            client.modes_paiement.add(payment_method)

        return client

    def update(self, instance, validated_data):
        addresses = validated_data.pop('adresses')
        payment_methods = validated_data.pop('modes_paiement')

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.adresses.clear()
        for address in addresses:
            address = Adresse.objects.get_or_create(**address)[0]
            instance.adresses.add(address)

        instance.modes_paiement.clear()
        for payment_method in payment_methods:
            payment_method = ModePaiement.objects.get_or_create(**payment_method)[0]
            instance.modes_paiement.add(payment_method)

        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class CommandeSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Commande
        fields = ('id', 'date', 'montant', 'etat', 'client')

    def create(self, validated_data):
        client = validated_data.pop('client')

        client = Client.objects.get_or_create(**client)[0]

        commande = Commande.objects.create(client=client, **validated_data)

        return commande

    def update(self, instance, validated_data):
        client = validated_data.pop('client')

        client = Client.objects.get_or_create(**client)[0]

        instance.client = client
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class LigneCommandeSerializer(serializers.ModelSerializer):
    commande = CommandeSerializer()
    produit = ProduitSerializer()

    class Meta:
        model = LigneCommande
        fields = ('id', 'commande', 'produit', 'quantite')

    def create(self, validated_data):
        commande = validated_data.pop('commande')
        produit = validated_data.pop('produit')

        commande = Commande.objects.get_or_create(**commande)[0]
        produit = Produit.objects.get_or_create(**produit)[0]

        ligne_commande = LigneCommande.objects.create(commande=commande, produit=produit, **validated_data)

        return ligne_commande

    def update(self, instance, validated_data):
        commande = validated_data.pop('commande')
        produit = validated_data.pop('produit')

        commande = Commande.objects.get_or_create(**commande)[0]
        produit = Produit.objects.get_or_create(**produit)[0]

        instance.commande = commande
        instance.produit = produit
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class RetourProduitSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer()

    class Meta:
        model = RetourProduit
        fields = ('id', 'produit', 'quantite', 'etat')

    def create(self, validated_data):
        produit = validated_data.pop('produit')

        produit = Produit.objects.get_or_create(**produit)[0]

        retour_produit = RetourProduit.objects.create(produit=produit, **validated_data)

        return retour_produit

    def update(self, instance, validated_data):
        produit = validated_data.pop('produit')

        produit = Produit.objects.get_or_create(**produit)[0]

        instance.produit = produit
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

