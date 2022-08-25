from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def saludo (request):
    return HttpResponse('Bienvenidos a todos ') #Prueba de servidor con la funcion saludo.

def index(request):
    return render (request, 'index.html')

    