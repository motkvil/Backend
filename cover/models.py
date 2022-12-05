from django.db import models

# Create your models here.
class Cover(models.Model):
    portada = models.URLField()
    encabezado = models.CharField(max_length=240)
    descripcion = models.TextField(max_length=1340)
    
    def __str__(self):
        return self.encabezado