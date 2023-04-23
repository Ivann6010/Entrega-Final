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
    reseña_pelicula = models.TextField(max_length=800)
    valoracion_final = models.CharField(max_length=100) 
    autorizado = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="autorizado")
    imagen = models.ImageField(upload_to="img")
    creado_el = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.id} - {self.nombre_pelicula} ({self.año_estreno})"

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    genero_preferido = models.CharField(max_length=100)
    pelicula_preferida = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="img-pro")

    def __str__(self):
        return f"{self.id} - {self.user}"

class Mensaje(models.Model):
    titulo = models.CharField(max_length=40)
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    receptor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="receptor")

