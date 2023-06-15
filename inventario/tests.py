from django.test import TestCase
from .models import Categoria


class TestCategorias(TestCase):
    def test_grabacion(self):
        categoria = Categoria(nombre="Bebidas")
        categoria.save()
        self.assertEqual(categoria.nombre, "Bebidas")

