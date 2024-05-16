from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, activity

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='home_product'),
    path('catalog/create/', ProductCreateView.as_view(), name='create_product'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/<int:pk>/activity/', activity, name='activity_product'),
]