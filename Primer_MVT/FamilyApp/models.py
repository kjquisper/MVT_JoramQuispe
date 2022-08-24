from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    hijos=models.IntegerField()
    nacimiento=models.DateField()
