from django.urls import path
from products.views import create_notebook,list_notebooks,create_monitor,list_monitors,create_peripherals,list_peripherals,search_products,\
    delete_notebook,update_notebook,delete_monitor,update_monitor , delete_peripheral , update_peripheral , Detail_notebook , Detail_peripheral , Detail_monitor

urlpatterns = [
    path ('new-notebook/',create_notebook,name='new-notebook'),
    path ('list-notebooks/',list_notebooks, name='list_notebooks'),
    path ('delete-notebook/<int:pk>/', delete_notebook, name='delete-notebook'),
    path ('update-notebook/<int:pk>/', update_notebook, name='update_notebook'),
    path ('detail-notebook/<int:pk>/', Detail_notebook.as_view(), name='Detail-notebook'),


    path ('new-monitor/',create_monitor,name='new-monitor'),
    path ('list-monitors/',list_monitors, name='list_monitors'),
    path ('delete-monitor/<int:pk>/', delete_monitor, name='delete-monitor'),
    path ('update-monitor/<int:pk>/', update_monitor, name='update_monitor'),
    path ('detail-monitor/<int:pk>/', Detail_monitor.as_view(), name='Detail_monitor'),
    

    path ('new-peripherals/',create_peripherals,name='new-peripherals'),
    path ('list-peripherals/',list_peripherals, name='list_peripherals'),
    path ('delete-peripheral/<int:pk>/', delete_peripheral, name='delete-peripheral'),
    path ('update-peripheral/<int:pk>/', update_peripheral, name='update_peripheral'),
    path ('detail-peripheral/<int:pk>/', Detail_peripheral.as_view(), name='detail-peripheral'),



    path ('search-products/',search_products, name='search_products')
]