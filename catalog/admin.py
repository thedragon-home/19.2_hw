from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost_of_purchase', 'category')
    list_filter = ('category',)
    search_fields = ('description','name',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'is_active',)
    list_filter = ('is_active',)