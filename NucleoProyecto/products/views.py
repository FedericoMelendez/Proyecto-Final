from django.shortcuts import render, redirect
from products.models import Notebooks, Monitores ,Perifericos
from products.forms import Formulario_notebooks, Formulario_monitores, Formulario_perifericos
from django.contrib.auth.decorators import login_required

#  Notebooks
@login_required
def create_notebook(request): #Crear Notebook

    if request.method == 'POST':
        form = Formulario_notebooks(request.POST)

        if form.is_valid():
            Notebooks.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'], 
                processor = form.cleaned_data['processor'],
                ram = form.cleaned_data['ram'],
                display = form.cleaned_data['display'],
                capacity = form.cleaned_data['capacity'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock']
            )

            return redirect(list_notebooks)

    elif request.method == 'GET':
            form = Formulario_notebooks()
            context = {'form':form}
            return render(request,'notebooks/new_notebook.html', context=context)


def list_notebooks(request):#Lista de Notebooks
    notebooks = Notebooks.objects.all() 
    context = {
        'notebooks':notebooks
        }
    return render(request, 'notebooks/list_notebooks.html', context=context)


# Monitores
@login_required
def create_monitor(request):#Crear Monitor
    if request.method == 'POST':
        form = Formulario_monitores(request.POST)

        if form.is_valid():
            Monitores.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'], 
                display = form.cleaned_data['display'],
                price = form.cleaned_data['price'],
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
@login_required
def create_peripherals(request):# Crear Perifericos
    if request.method == 'POST':
        form = Formulario_perifericos(request.POST)

        if form.is_valid():
            Perifericos.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'], 
                type = form.cleaned_data['type'],
                price = form.cleaned_data['price'],
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
    notebooks =Notebooks.objects.filter(name__icontains=search)
    monitors = Monitores.objects.filter(name__icontains=search)
    peripherals = Perifericos.objects.filter(name__icontains=search)
    context = {
        'notebooks':notebooks,
        'monitors':monitors,
        'peripherals':peripherals
    }
    return render(request, 'search_products.html', context=context)