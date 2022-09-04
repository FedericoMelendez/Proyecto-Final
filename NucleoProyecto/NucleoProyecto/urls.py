from itertools import product
from operator import index
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from NucleoProyecto.views import saludo,index, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludo/', saludo, name='saludo'), #Prueba del servidor con la funcion saludo
    path('products/',include ('products.urls')),
    path ('', index, name='index'),
    path ('index/', index, name='index'),
    path('users/', include ('users.urls')),
    path ('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
