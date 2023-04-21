from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    nombre_pelicula = models.CharField(max_length=40)
    año_estreno = models.IntegerField(validators=[
        MinValueValidator(1895),
        MaxValueValidator(timezone.now().year)])
    reseña_pelicula = models.CharField(max_length=800)
    valoracion_final = models.CharField(max_length=50) 
    autorizado = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="autorizado")
    imagen = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nombre_pelicula} ({self.año_estreno})"
