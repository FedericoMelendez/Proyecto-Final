from operator import index
from django.contrib import admin
from django.urls import path
from NucleoProyecto.views import saludo



urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludo/', saludo, name='saludo'), #Prueba del servidor con la funcion saludo

]
