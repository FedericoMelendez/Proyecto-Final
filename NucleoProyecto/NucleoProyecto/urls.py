from itertools import product
from operator import index
from django.contrib import admin
from django.urls import path,include
from NucleoProyecto.views import saludo,index


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludo/', saludo, name='saludo'), #Prueba del servidor con la funcion saludo
    path('products/',include ('products.urls')),
    path ('', index, name='index')
]
