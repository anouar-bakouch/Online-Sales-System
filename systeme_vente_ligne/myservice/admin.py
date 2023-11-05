from django.contrib import admin

# Register your models here.
from .models import Produit , Adresse , Client , ModePaiement , Commande , LigneCommande , RetourProduit

admin.site.register(Produit)
admin.site.register(Adresse)
admin.site.register(Client)
admin.site.register(ModePaiement)
admin.site.register(Commande)
admin.site.register(LigneCommande)
admin.site.register(RetourProduit)
