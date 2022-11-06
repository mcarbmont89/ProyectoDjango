from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from appcoder.models import Familiares

# Create your views here.
def vista_listado_familiares(request):
    familiares = Familiares.objects.all()
    data={"familiares":familiares,}
    plantilla = loader.get_template("listado_familiares.html")
    respuesta = plantilla.render(data)
    return HttpResponse(respuesta)