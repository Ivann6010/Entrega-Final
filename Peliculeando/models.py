from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    nombre_pelicula = models.CharField(max_length=40)

    año_estreno = models.IntegerField(validators=[
        MinValueValidator(1895),
        MaxValueValidator(timezone.now().year)])

    reseña_pelicula = models.CharField(max_length=800)

    valoracion_final = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.id} - {self.nombre_pelicula} ({self.año_estreno})"
