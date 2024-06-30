from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=10)
    nom_cli = models.CharField(max_length=20, null=False)
    appa_cli = models.CharField(max_length=20, null=False)
    apma_cli = models.CharField(max_length=20, null=False)
