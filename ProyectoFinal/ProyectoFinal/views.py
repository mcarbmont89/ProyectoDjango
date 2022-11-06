from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import os

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
    archivo = open(r"C:\Users\maria\OneDrive\Documents\Coder House\Python\ProyectoDjango\ProyectoFinal\ProyectoFinal\templates\plantilla_bonita.html", encoding="utf-8")
    plantilla = Template(archivo.read())
    archivo.close()
    datos = {"nombre":"Maria", "apellido":"Carbajal","fecha":datetime.now()}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    archivo = open(r"C:\Users\maria\OneDrive\Documents\Coder House\Python\ProyectoDjango\ProyectoFinal\ProyectoFinal\templates\listado.html", encoding="utf-8")
    plantilla = Template(archivo.read())
    archivo.close()
    listado_alumnos = ["Juan Lopez", "Nadia Cepeda","Ari Borovoy"]
    datos = {"tecnologia":"React", "listado_alumnos":listado_alumnos}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    plantilla = loader.get_template("listado.html")
    listado_alumnos = ["Pedro Martinez", "Nicolas Uceda","Rachel Shapiro"]
    datos = {"tecnologia":"Python", "listado_alumnos":listado_alumnos}
    documento = plantilla.render(datos)
    return HttpResponse(documento)