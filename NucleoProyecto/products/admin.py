from django.contrib import admin
from products.models import Notebooks,Monitores,Perifericos

@admin.register(Notebooks)
class Notebooks_admin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model','processor','ram','display','capacity','price','stock','is_active']

@admin.register(Monitores)
class Monitores_admin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model','display','price','stock','is_active']

@admin.register(Perifericos)
class Perifericos_admin(admin.ModelAdmin):
    list_display = ['name', 'brand','type','price','stock','is_active']