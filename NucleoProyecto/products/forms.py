from socket import fromshare
from django import forms

class Form_notebooks(forms.Form):
    name = forms.CharField(max_length=200) #Nombre 
    brand = forms.CharField(max_length=50) #Marca
    model = forms.CharField(max_length=100) #Modelo
    processor = forms.CharField(max_length=100) #Procesador
    ram = forms.CharField(max_length=100) #Capacidad de Memoria RAM
    display = forms.CharField(max_length=50) # Tamaño de pantalla
    capacity = forms.CharField(max_length=50) # Capacidad de almacenamiento
    price = forms.FloatField() #Precio
    is_active = forms.BooleanField(default=True)
    stock = forms.IntegerField()
    