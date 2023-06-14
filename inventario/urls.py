from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/<str:name>", views.contact),
    path("categorias/", views.categorias),
]
