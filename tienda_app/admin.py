from django.contrib import admin
from .models import Libro, Inventario, Orden

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'precio']

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'libro', 'cantidad']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'libro', 'total']