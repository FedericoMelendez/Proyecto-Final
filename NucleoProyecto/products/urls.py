from django.urls import path
from products.views import create_notebook,list_notebooks,create_monitor,list_monitors,create_peripherals,list_peripherals,search_products,list_all

urlpatterns = [
    path ('new-notebook/',create_notebook,name='new-notebook'),
    path ('list-notebooks/',list_notebooks, name='list_notebooks'),


    path ('new-monitor/',create_monitor,name='new-monitor'),
    path ('list-monitors/',list_monitors, name='list_monitors'),

    path ('new-peripherals/',create_peripherals,name='new-peripherals'),
    path ('list-peripherals/',list_peripherals, name='list_peripherals'),


    path ('search-products/',search_products, name='search_products'),
    path ('all-products/',list_all, name='all-products')
]