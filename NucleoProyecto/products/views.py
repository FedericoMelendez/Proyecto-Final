from django.shortcuts import render, redirect
from products.models import Notebooks, Monitores ,Perifericos
from products.forms import Formulario_notebooks, Formulario_monitores, Formulario_perifericos

#  Notebooks

def create_notebook(request):#Crear Notebook
    if request.method == 'POST':
        form = Formulario_notebooks(request.POST)

        if form.is_valid():
            Notebooks.objects.create(
                name = form.cleaned_data['nombre'],
                brand = form.cleaned_data['marca'],
                model = form.cleaned_data['modelo'], 
                proccesor = form.cleaned_data['procesador'],
                ram = form.cleaned_data['ram'],
                display = form.cleaned_data['pantalla'],
                capacity = form.cleaned_data['almacenamiento'],
                price = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(list_notebooks)

        elif request.method == 'GET':
            form = Formulario_notebooks()
            context = {'form':form}
            return render(request, 'notebooks/new_notebook.html', context=context)

def list_notebooks(request):#Lista de Notebooks
    notebooks = Notebooks.objects.all() 
    context = {
        'notebooks':notebooks
        }
    return render(request, 'notebooks/list_notebooks.html', context=context)


# Monitores

def create_monitor(request):#Crear Monitor
    if request.method == 'POST':
        form = Formulario_monitores(request.POST)

        if form.is_valid():
            Monitores.objects.create(
                name = form.cleaned_data['nombre'],
                brand = form.cleaned_data['marca'],
                model = form.cleaned_data['modelo'], 
                display = form.cleaned_data['pantalla'],
                price = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(list_monitors)

        elif request.method == 'GET':
            form = Formulario_monitores()
            context = {'form':form}
            return render(request, 'monitors/new_monitor.html', context=context)

def list_monitors(request):#Lista de Monitores
    monitors = Monitores.objects.all() 
    context = {
        'monitores':monitors
        }
    return render(request, 'monitors/list_monitors.html', context=context)

# Perifericos 

def create_peripherals(request):# Crear Perifericos
    if request.method == 'POST':
        form = Formulario_perifericos(request.POST)

        if form.is_valid():
            Perifericos.objects.create(
                name = form.cleaned_data['nombre'],
                brand = form.cleaned_data['marca'], 
                type = form.cleaned_data['tipo'],
                price = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(list_peripherals)

        elif request.method == 'GET':
            form = Formulario_perifericos()
            context = {'form':form}
            return render(request, 'peripherals/new_peripherals.html', context=context)

def list_peripherals(request):# Lista de Perifericos
    peripherals = Perifericos.objects.all() 
    context = {
        'perifericos':peripherals
        }
    return render(request, 'peripherals/list_peripherals.html', context=context)


def list_all(request):
    all_peripherals = Perifericos.objects.all()
    all_monitors = Monitores.objects.all()
    all_notebooks = Notebooks.objects.all()
    context = {
        'perifericos':all_peripherals,
        'monitores':all_monitors,
        'notebooks':all_notebooks
        }
    return render(request, 'all_products.html', context=context)

def search_products(request): #Busqueda de todos los productos
    search = request.GET['search']
    products_notebooks =Notebooks.objects.filter(name__icontains=search)
    products_monitors = Monitores.objects.filter(name__icontains=search)
    products_peripherals = Perifericos.objects.filter(name__icontains=search)
    context = {
        'products_notebooks': products_notebooks,
        'products_monitors': products_monitors,
        'products_peripherals':products_peripherals
    }
    return render(request, 'search_products.html', context=context)