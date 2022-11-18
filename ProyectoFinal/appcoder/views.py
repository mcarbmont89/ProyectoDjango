from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from appcoder.models import *

def inicio(request):
    return render(request,"appcoder/index.html")
def cursos(request):
    return HttpResponse("Estas en cursos")
def estudiantes(request):
    return HttpResponse("Estas en estudiantes")
def profesores(request):
    return HttpResponse("Estas en profesores")
def entregables(request):
    return HttpResponse("Estas en entregables")

def vista_listado_familiares(request):
    familiares = Familiares.objects.all()
    data={"familiares":familiares,}
    plantilla = loader.get_template("listado_familiares.html")
    respuesta = plantilla.render(data)
    return HttpResponse(respuesta)