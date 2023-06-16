from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)


urlpatterns = [
    # path("", views.index, name="index"),
    path("contact/<str:name>", views.contact),
    # path("categorias/", views.categorias, name="categorias"),
    # path("productos/", views.productoFormView, name="productos"),
    path("categorias/cantidad", views.categoria_count, name="categoria_count"),
    path("productos/filtrar/unidades", views.producto_en_unidades),
    path("reporte/productos", views.reporte_productos),
    path("categorias_crear_listar", views.CategoriaCreateView.as_view(), name="categorias_crear"),
    path("", include(router.urls)),
]
