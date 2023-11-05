from django.contrib import admin
from django.urls import path
from myservice.views import index,ProduitAPIView,ClientAPIView,CommandeAPIView,ModePaiementAPIView,AdresseAPIView,RetourProduitAPIView,LigneCommandeAPIView

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('api/produits/', ProduitAPIView.as_view(), name='produits'),
    path('api/clients/',ClientAPIView.as_view(),name='clients'),
    path('api/commandes/',CommandeAPIView.as_view(),name='Commande'),
    path('api/modes_paiement/',ModePaiementAPIView.as_view(),name='modepaiement'),
    path('api/adresses/',AdresseAPIView.as_view(),name='adresses'),
    path('api/remboursement/',RetourProduitAPIView.as_view(),name='remboursement'),
    path('api/ligneCommande/',LigneCommandeAPIView.as_view(),name='ligne commande'),
]
