from django.contrib.auth.models import User
from rest_framework import serializers

class Enregistrementutilisateur(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def createUtilisateur(self, validated_data):
        utilisateur = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return utilisateur