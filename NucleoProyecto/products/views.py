from django.views.generic import DetailView
from django.shortcuts import render, redirect
from products.models import Notebooks, Monitores ,Perifericos
from products.forms import Formulario_notebooks, Formulario_monitores, Formulario_perifericos
from django.contrib.auth.decorators import login_required




#  Notebooks
@login_required
def create_notebook(request): #Crear Notebook

    if request.method == 'POST':
        form = Formulario_notebooks(request.POST, request.FILES)

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
                stock = form.cleaned_data['stock'],
                image=form.cleaned_data['image']
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

@login_required
def delete_notebook (request, pk):
    if request.method == 'GET':
        notebook = Notebooks.objects.get(pk=pk)
        context = {'notebook':notebook}
        return render(request, 'notebooks/delete_notebook.html', context=context)
    elif request.method == 'POST':
        notebook = Notebooks.objects.get(pk=pk)
        notebook.delete()
        return redirect(list_notebooks)

@login_required
def update_notebook(request, pk):
    if request.method == 'POST':
        form = Formulario_notebooks(request.POST, request.FILES)
        if form.is_valid():
            notebook = Notebooks.objects.get(id=pk)
            notebook.name = form.cleaned_data['name']
            notebook.brand = form.cleaned_data['brand']
            notebook.model = form.cleaned_data['model']
            notebook.processor = form.cleaned_data['processor']
            notebook.ram = form.cleaned_data['ram']
            notebook.display = form.cleaned_data['display']
            notebook.capacity = form.cleaned_data['capacity']
            notebook.price = form.cleaned_data['price']
            notebook.stock = form.cleaned_data['stock']
            if form.cleaned_data['image']:
                notebook.image=form.cleaned_data['image']
            notebook.save()
            return redirect(list_notebooks)


    elif request.method == 'GET':
        notebook = Notebooks.objects.get(id=pk)

        form = Formulario_notebooks(initial={
                                        'name':notebook.name,
                                        'brand':notebook.brand,
                                        'model':notebook.model,
                                        'processor':notebook.processor,
                                        'ram':notebook.ram,
                                        'display':notebook.display,
                                        'capacity':notebook.capacity, 
                                        'price':notebook.price,
                                        'stock':notebook.stock,
                                        'image':notebook.image})
        context = {'form':form}
        return render(request, 'notebooks/update_notebook.html', context=context)


class Detail_notebook(DetailView):
    model= Notebooks
    template_name= 'notebooks/detail_notebook.html'

# Monitores
@login_required
def create_monitor(request):#Crear Monitor
    if request.method == 'POST':
        form = Formulario_monitores(request.POST, request.FILES)

        if form.is_valid():
            Monitores.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'], 
                display = form.cleaned_data['display'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock'],
                image=form.cleaned_data['image']
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

@login_required
def delete_monitor (request, pk):
    if request.method == 'GET':
        monitor = Monitores.objects.get(pk=pk)
        context = {'monitor':monitor}
        return render(request, 'monitors/delete_monitor.html', context=context)
    elif request.method == 'POST':
        monitor = Monitores.objects.get(pk=pk)
        monitor.delete()
        return redirect(list_monitors)

@login_required
def update_monitor(request, pk):
    if request.method == 'POST':
        form = Formulario_monitores(request.POST, request.FILES)
        if form.is_valid():
            monitor = Monitores.objects.get(id=pk)
            monitor.name = form.cleaned_data['name']
            monitor.brand = form.cleaned_data['brand']
            monitor.model = form.cleaned_data['model']
            monitor.display = form.cleaned_data['display']
            monitor.price = form.cleaned_data['price']
            monitor.stock = form.cleaned_data['stock']
            if form.cleaned_data['image']:
                monitor.image=form.cleaned_data['image']
            monitor.save()

            return redirect(list_monitors)


    elif request.method == 'GET':
        monitor = Monitores.objects.get(id=pk)

        form = Formulario_monitores(initial={
                                        'name':monitor.name,
                                        'brand':monitor.brand,
                                        'model':monitor.model,
                                        'display':monitor.display,
                                        'price':monitor.price,
                                        'stock':monitor.stock,
                                        'image':monitor.image})
        context = {'form':form}
        return render(request, 'monitors/update_monitor.html', context=context)


class Detail_monitor(DetailView):
    model= Monitores
    template_name= 'monitors/detail_monitor.html'


# Perifericos 
@login_required
def create_peripheral(request):# Crear Perifericos
    if request.method == 'POST':
        form = Formulario_perifericos(request.POST,request.FILES)

        if form.is_valid():
            Perifericos.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'], 
                type = form.cleaned_data['type'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock'],
                image = form.cleaned_data['image']
            )

            return redirect(list_peripherals)

    elif request.method == 'GET':
            form = Formulario_perifericos()
            context = {'form':form}
            return render(request, 'peripherals/new_peripheral.html', context=context)

def list_peripherals(request):# Lista de Perifericos
    peripherals = Perifericos.objects.all() 
    context = {
        'perifericos':peripherals
        }
    return render(request, 'peripherals/list_peripherals.html', context=context)

@login_required
def delete_peripheral (request, pk):
    if request.method == 'GET':
        peripheral = Perifericos.objects.get(pk=pk)
        context = {'peripheral':peripheral}
        return render(request, 'peripherals/delete_peripheral.html', context=context)
    elif request.method == 'POST':
        peripheral = Perifericos.objects.get(pk=pk)
        peripheral.delete()
        return redirect(list_peripherals)

@login_required
def update_peripheral(request, pk):
    if request.method == 'POST':
        form = Formulario_perifericos(request.POST,request.FILES)
        if form.is_valid():
            peripherals = Perifericos.objects.get(id=pk)
            peripherals.name = form.cleaned_data['name']
            peripherals.brand = form.cleaned_data['brand']
            peripherals.type = form.cleaned_data['type']
            peripherals.price = form.cleaned_data['price']
            peripherals.stock = form.cleaned_data['stock']
            if form.cleaned_data['image']:
                peripherals.image = form.cleaned_data['image']
            peripherals.save()

            return redirect(list_peripherals)


    elif request.method == 'GET':
        peripherals = Perifericos.objects.get(id=pk)

        form = Formulario_perifericos(initial={
                                        'name':peripherals.name,
                                        'brand':peripherals.brand,
                                        'type':peripherals.type,
                                        'price':peripherals.price,
                                        'stock':peripherals.stock,
                                        'image':peripherals.image})
        context = {'form':form}
        return render(request, 'peripherals/update_peripheral.html', context=context)



class Detail_peripheral(DetailView): #Detalle de los perifericos
    model= Perifericos
    template_name= 'peripherals/detail_peripheral.html'



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


def all_products(request):# Lista de todos los productos
    notebooks =Notebooks.objects.all()
    monitors = Monitores.objects.all()
    peripherals = Perifericos.objects.all()
    context = {
        'notebooks':notebooks,
        'monitors':monitors,
        'peripherals':peripherals
    }
    return render(request, 'all_products.html', context=context)
