from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduitAPIView
from .views import InscriptionAPIView, ConnexionAPIView
#router = DefaultRouter()
#router.register(r'produits', ProduitViewSet)

urlpatterns = [
    path('produits/', ProduitAPIView.as_view(), name='produit-list'),
    path('inscription/', InscriptionAPIView.as_view(), name='inscription'),
    path('connexion/', ConnexionAPIView.as_view(), name='connexion'),
]