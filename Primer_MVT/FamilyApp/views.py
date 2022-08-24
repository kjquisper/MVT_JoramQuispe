from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
from django.template import loader
# Create your views here.

def familiar(render):
    familiar1 = Familiar(nombre="Fernanda Casas",hijos=2,nacimiento="1937-10-2")
    familiar2 = Familiar(nombre="Juan Gonzales",hijos=3,nacimiento="1908-10-2")
    familiar3 = Familiar(nombre="Luis Gonzales",hijos=2,nacimiento="1992-10-2")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    diccionario={'familiar1':familiar1 ,'familiar2':familiar2,'familiar3':familiar3}
    plantilla=loader.get_template('Template1.html')
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)
    
