from django.db import models
from AppUsuarios.models import Usuario

class Empresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.razon_social
