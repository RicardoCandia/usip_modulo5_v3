from django.contrib import admin
from .models import Categoria
from .models import Producto

# Register your models here.
"""
CATEGORIA
"""
admin.site.register(Categoria)

"""
PRODUCTO
"""
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'categoria__nombre')
    ordering = ('nombre', 'precio')

admin.site.register(Producto, ProductoAdmin)
