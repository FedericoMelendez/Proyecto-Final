from django.urls import path
from products.views import create_notebook

urlpatterns = [
    path ('new-notebook/',create_notebook,name='create_notebook'),

    path ('list-notebooks/',lista_notebooks, name='lista_notebooks'),
    path ('search-notebooks/',search_notebooks, name='search_notebooks'),
    path ('delete-notebook/<int:pk>/',delete_notebook, name='delete_notebook')

]