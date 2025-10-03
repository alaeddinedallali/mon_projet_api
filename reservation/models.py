from django.db import models

#class Produit(models.Model):
 #   nom = models.CharField(max_length=100)
  #  prix = models.DecimalField(max_digits=10, decimal_places=2)

   # def __str__(self):
    #    return self.nom 

class Reservation(models.Model):
    nom_client = models.CharField(max_length=100)
    numero_train = models.IntegerField()
    carte_transport=models.BooleanField(default=False)
    date_reservation = models.DateTimeField()
    nombre_personnes = models.IntegerField()

    def __str__(self):
        return f"Réservation de {self.nom_client} pour le train {self.numero_train} le {self.date_reservation}"