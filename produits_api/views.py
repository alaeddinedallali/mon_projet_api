from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

from .auth_serializers import Enregistrementutilisateur
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class ProduitAPIView(APIView):
    # Récupérer tous les produits
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    # Créer un produit
    def post(self, request):
        serializer = Enregistrementutilisateur(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InscriptionAPIView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = Enregistrementutilisateur(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.createUtilisateur(serializer.validated_data)
            return Response({
                "status": "Utilisateur créé avec succès",
                "username": utilisateur.username,
                "massage": "Vous pouvez maintenant vous connecter"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConnexionAPIView(APIView):
    permission_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        utilisateur = authenticate(username=username, password=password)
        if utilisateur:
            token, created = Token.objects.get_or_create(user=utilisateur)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)