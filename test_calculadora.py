import unittest

from Calculadora import calcular

class TestMethod(unittest.TestCase):

  def test_soma(self):
    self.assertEqual(calcular('+', 1, 1), 2, "Precisa ser 2")

  def test_subtracao(self):
    self.assertEqual(calcular('-', 1, 1), 0, "Precisa ser 0")

  def test_multiplicacao(self):
    self.assertEqual(calcular('*', 2, 5), 10,  "Precisa ser 10")

  def test_divisao(self):
    self.assertEqual(calcular('/', 10, 2), 5,  "Precisa ser 5")