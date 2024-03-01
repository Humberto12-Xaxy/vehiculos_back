from django.db import models

class Vehiculo(models.Model):

    placas = models.CharField(max_length = 17)
    latitud = models.FloatField(null = False)
    longitud = models.FloatField(null = False)
    user_id = models.IntegerField(null = False)