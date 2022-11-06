# ProyectoDjango

URL de consulta: http://127.0.0.1:8000/

Template: listado_familiares.html (ProyectoFinal/Templates)
Vista: vista_listado_familiares (appcoder/views.py) 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado de familiares</title>
</head>
<body>
    <h1>Mi familia</h1>
    <table>
        <tr>
          <th>id</th>
          <th>Nombre</th>
          <th>Cumple</th>
          <th>Recidencia</th>
        </tr>
        {% for familiar in familiares %}
        <tr>
            <td>{{familiar.id}}</td>
            <td>{{familiar.nombre}}</td>
            <td>{{familiar.fechaDeNacimiento}}</td>
            <td>{{familiar.ciudad}}</td>
        </tr>
        {% endfor %}
        </table>
      
</body>
</html>

def vista_listado_familiares(request):
    familiares = Familiares.objects.all()
    data={"familiares":familiares,}
    plantilla = loader.get_template("listado_familiares.html")
    respuesta = plantilla.render(data)
    return HttpResponse(respuesta)
    
Modelo: Familiares (appcoder/models.py)
  
  class Familiares(models.Model):
      nombre=models.CharField(max_length=40)
      fechaDeNacimiento=models.DateField(("Date"), default=datetime.now())
      ciudad=models.CharField(max_length=40)
