from django.db import models

# Create your models here.
class Produit(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)
  description = models.TextField()
  prix = models.FloatField()
  stock = models.IntegerField()

  def __str__(self):
    return self.nom

class Adresse(models.Model):
  id = models.AutoField(primary_key=True)
  adresse = models.CharField(max_length=255)
  code_postal = models.CharField(max_length=255)
  ville = models.CharField(max_length=255)

  def __str__(self):
    return self.adresse

class ModePaiement(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)

  def __str__(self):
    return self.nom

class Client(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=255)
  email = models.EmailField()
  adresses = models.ManyToManyField(Adresse)
  modes_paiement = models.ManyToManyField(ModePaiement)
  points_fidelite = models.IntegerField()

  def __str__(self):
    return self.nom

class Commande(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateTimeField()
  etat = models.CharField(max_length=255,choices=[
        ('en cours de traitement', 'En cours de traitement'),
        ('expédiée', 'Expédiée'),
        ('livrée', 'Livrée'),
        ('annulée', 'Annulée')
    ])
  client = models.ForeignKey(Client,on_delete=models.CASCADE)

  def __str__(self):
    return self.etat 


class LigneCommande(models.Model):
  id = models.AutoField(primary_key=True)
  commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
  produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
  quantite = models.IntegerField()
  montant = models.FloatField()
  
  def __str__(self):
    return self.produit.nom 


class RetourProduit(models.Model): # remboursement
  id = models.AutoField(primary_key=True)
  produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
  quantite = models.IntegerField()
  etat = models.CharField(max_length=255)

