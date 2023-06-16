from django.test import TestCase
from .models import Categoria
from django.core.exceptions import ValidationError


class TestCategorias(TestCase):
    def test_grabacion(self):
        categoria = Categoria(nombre="Bebidas")
        categoria.save()
        self.assertEqual(categoria.nombre, "Bebidas")

    def test_grabacion_db(self):
        q = Categoria.objects.create(nombre="No permitido")
        self.assertRaises(ValidationError, q.full_clean)

    def test_grabacion_db_mensaje(self):
        with self.assertRaises(ValidationError) as qv:
            q = Categoria.objects.create(nombre="No permitido")
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0], "No es una opcion permitida")
