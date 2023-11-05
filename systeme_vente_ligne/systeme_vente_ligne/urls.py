from django.contrib import admin
from django.urls import path
from myservice.views import index,ProduitAPIView,ClientAPIView,CommandeAPIView

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('api/produits/', ProduitAPIView.as_view(), name='produits'),
    path('api/clients/',ClientAPIView.as_view(),name='clients'),
    path('api/commandes/',CommandeAPIView.as_view(),name='Commande'),

]
