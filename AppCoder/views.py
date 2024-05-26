from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.


def curso(req, name, camada):

    nuevo_curso = Curso(name=name, camada=camada)
    nuevo_curso.save()

    return HttpResponse(f"""
        <p>Curso: {nuevo_curso.name} - Camada:{nuevo_curso.camada} creado!!</p>
    """)


def lista_cursos(req):
    lista = Curso.objects.all()

    # con el método render que ya está importado mostramos los datos de la tabla que solicitamos antes en un html

    # lo que esta entre {} es el contexto
    return render(req, "lista_cursos.html", {"lista_cursos": lista})
