from django.db import models

class auto(models.Model):
    id_auto     = models.AutoField(primary_key=True)
    marca       = models.CharField(max_length=20,null=False)
    modelo      = models.CharField(max_length=20,null=False)
    año         = models.IntegerField()
    transmision = models.CharField(max_length=20)
    motor       = models.CharField(max_length=20)   
    img         = models.ImageField(upload_to='img/',null=False)
    velocidades = models.IntegerField()
    precio      = models.IntegerField(null=False)
    stock       = models.IntegerField(null=False)

    def __str__(self):
        return str(self.marca)+" "+str(self.modelo) 
