from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import os
from appcoder.models import Familiares

# Create your views here.
def vista_listado_familiares(request):
    familiares = Familiares.objects.all()
    data={"familiares":familiares,}
    plantilla = loader.get_template("listado_familiares.html")
    respuesta = plantilla.render(data)
    return HttpResponse(respuesta)

def vista_saludo(request):
    return HttpResponse("""<h1>Hola coders!</h1>
    <p style='color:red'> Esto es una prueba </p>
    """)
def inicia_sesion(request):
    return HttpResponse("Tu user y password")

def dia_hoy(request, nombre):
    hoy=datetime.now()
    respuesta=f"Hoy es {hoy} - Bienvenid@ {nombre}"
    return HttpResponse(respuesta)

def anio_nacimiento(request,edad):
    edad = int(edad)
    anio_nac=datetime.now().year-edad
    return HttpResponse(f"Naciste en  {anio_nac}")

def vista_plantilla(request):
    plantilla = loader.get_template("plantilla_bonita.html")
    datos = {"nombre":"Maria", "apellido":"Carbajal","fecha":datetime.now()}
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    plantilla = loader.get_template("listado.html")
    listado_alumnos = ["Juan Lopez", "Nadia Cepeda","Ari Borovoy"]
    datos = {"tecnologia":"React", "listado_alumnos":listado_alumnos}
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    plantilla = loader.get_template("listado.html")
    listado_alumnos = ["Pedro Martinez", "Nicolas Uceda","Rachel Shapiro"]
    datos = {"tecnologia":"Python", "listado_alumnos":listado_alumnos}
    documento = plantilla.render(datos)
    return HttpResponse(documento)