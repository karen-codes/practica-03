import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_ventas_totales_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_numero_provincias_coherente(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        # Debe haber entre 20 y 30 provincias en el dataset
        self.assertGreaterEqual(len(resumen), 20)
        self.assertLessEqual(len(resumen), 30)

    def test_valores_no_negativos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(v >= 0 for v in resumen.values()))

    def test_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertGreater(resultado, 0)
    def test_exportaciones_por_mes(self):
        resultado = self.analizador.exportaciones_por_mes()
        self.assertIsInstance(resultado, dict)
        self.assertTrue(all(mes > 0 for mes in resultado.keys()))

    def test_provincia_mayor_importacion(self):
        resultado = self.analizador.provincia_mayor_importacion()
        self.assertIsInstance(resultado, str)
        self.assertTrue(len(resultado) > 0)
