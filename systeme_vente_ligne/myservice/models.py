from django.db import models

# Create your models here.
class Produit(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)
  description = models.TextField()
  prix = models.FloatField()
  stock = models.IntegerField()

class Adresse(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)
  prenom = models.CharField(max_length=255)
  adresse = models.CharField(max_length=255)
  code_postal = models.CharField(max_length=255)
  ville = models.CharField(max_length=255)

class ModePaiement(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)

class Client(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)
  email = models.EmailField()
  adresses = models.ManyToManyField(Adresse)
  modes_paiement = models.ManyToManyField(ModePaiement)
  points_fidelite = models.IntegerField()

class Commande(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateTimeField()
  montant = models.FloatField()
  etat = models.CharField(max_length=255)
  client = models.ForeignKey(Client,on_delete=models.CASCADE)


class LigneCommande(models.Model):
  id = models.AutoField(primary_key=True)
  commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
  produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
  quantite = models.IntegerField()


class RetourProduit(models.Model):
  id = models.AutoField(primary_key=True)
  produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
  quantite = models.IntegerField()
  etat = models.CharField(max_length=255)

