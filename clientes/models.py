from django.db import models

# Create your models here.

class Cliente(models.Model):
    Correo = models.EmailField(primary_key=True, max_length=10)
    Nombre = models.CharField(max_length=20, null=False)
    Clave = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.Nombre
