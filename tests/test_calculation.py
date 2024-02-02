# Verificar se as funções responsáveis pelos cálculos retornam os resultados esperados para uma variedade de entradas
# Identificar as funções no seu código que realizam cálculos críticos.
# Escrever casos de teste que fornecem diferentes conjuntos de entradas para essas funções.
# Verificar se os resultados produzidos pelas funções correspondem aos resultados esperados para cada conjunto de entradas.
import unittest
from geometric_shapes import calcular_area_volume, verificar_tipo_forma

class TestGeometricShapes(unittest.TestCase):
    def test_calcular_area_volume(self):
        # Testes para formas bidimensionais
        self.assertEqual(calcular_area_volume("quadrado", 2), (4, None))
        self.assertEqual(calcular_area_volume("retangulo", 3, 4), (12, None))
        self.assertEqual(calcular_area_volume("triangulo", 4, 5), (10, None))
        self.assertAlmostEqual(calcular_area_volume("circulo", 2)[0], 12.5663706144, places=6)

        # Testes para formas tridimensionais
        self.assertEqual(calcular_area_volume("cilindro", 2, 3), (37.69911184307752, 94.24777960769379, 37.69911184307752))
        self.assertEqual(calcular_area_volume("esfera", 4), (201.06192982974676, 268.082573106329, ))
        self.assertEqual(calcular_area_volume("cubo", 3), (54, 27))
        self.assertEqual(calcular_area_volume("paralelepipedo", 2, 3, 4), (52, 24))

    def test_verificar_tipo_forma(self):
        self.assertEqual(verificar_tipo_forma("quadrado"), "bidimensional")
        self.assertEqual(verificar_tipo_forma("esfera"), "tridimensional")
        self.assertEqual(verificar_tipo_forma("piramide"), "Forma não reconhecida")

if __name__ == '__main__':
    unittest.main()
