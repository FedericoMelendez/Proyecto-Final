from django.shortcuts import render, redirect
from products.models import Notebooks, Monitores ,Perifericos
from products.forms import Formulario_notebooks, Formulario_monitores, Formulario_perifericos


#  Notebooks

def create_notebook(request):
    if request.method == 'POST':
        form = Formulario_notebooks(request.POST)

        if form.is_valid():
            Notebooks.objects.create(
                name = form.cleaned_data['nombre'],
                brand = form.cleaned_data['marca'],
                model = form.cleaned_data['modelo'], 
                proccesor = form.cleaned_data['procesador'],
                ram = form.cleaned_data['ram'],
                display = form.cleaned_data['pulgadas'],
                capacity = form.cleaned_data['almacenamiento'],
                price = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )

            return redirect(list_notebooks)

        elif request.method == 'GET':
            form = Formulario_notebooks()
            context = {'form':form}
            return render(request, 'notebooks/new_notebook.html', context=context)

def list_notebooks(request):
    notebooks = Notebooks.objects.all() 
    context = {
        'notebooks':notebooks
        }
    return render(request, 'notebooks/list_notebooks.html', context=context)


# Monitores



