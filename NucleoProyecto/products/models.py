from django.db import models

class Notebooks(models.Model): 
    name = models.CharField(max_length=200) #Nombre 
    brand = models.CharField(max_length=50) #Marca
    model = models.CharField(max_length=100) #Modelo
    processor = models.CharField(max_length=100) #Procesador
    ram = models.CharField(max_length=100) #Capacidad de Memoria RAM
    display = models.CharField(max_length=50) # Tamaño de pantalla
    capacity = models.CharField(max_length=50) # Capacidad de almacenamiento
    price = models.FloatField() #Precio
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='notebooks/', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'

class Monitores (models.Model): 
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    display = models.CharField(max_length=50)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'

class Perifericos (models.Model): 
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Periferico'
        verbose_name_plural = 'Perifericos'


