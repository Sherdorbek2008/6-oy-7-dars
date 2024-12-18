from django.db import models

class Tur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Gul(models.Model):
    nom = models.CharField(max_length=100)
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE, related_name="gullar")

    def __str__(self):
        return self.nom
