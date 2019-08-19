from django.core.validators import MaxValueValidator,MinValueValidator
from django.db import models

class Geogebra(models.Model):
    id_geogebra = models.CharField(max_length=50)
    titre = models.CharField(max_length=100)
    width = models.IntegerField(default=800,validators=[MaxValueValidator(1000),MinValueValidator(1)])
    height = models.IntegerField(default=600,validators=[MaxValueValidator(1000),MinValueValidator(1)])

    def __str__(self):
        return self.titre
