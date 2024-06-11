from django.shortcuts import render
from .models import Alumno,Genero
# Create your views here.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()

def index(request):
    hijo = Persona("Pickles", 7)
    lista = ["lazaña", "charquicán", "porotos granados"]

    alumnos = Alumno.objects.all()


    context = {"hijo": hijo, "nombre": "claudia andrea", "comidas": lista, "alumnos":alumnos } 
    
    return render(request, 'alumnos/index.html', context)
