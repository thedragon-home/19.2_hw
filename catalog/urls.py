from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, home_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', home_product, name='home_product')
]