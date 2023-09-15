import unittest
from calculadora_horas import CalculadoraHoras

class TestCalculadoraHoras(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraHoras()

    def test_inserir_horarios_formato_Hmm(self):
        resultado = self.calculadora.inserir_horarios("2023-09-14", "900", "1700")
        self.assertEqual(resultado, None)
        self.assertEqual(self.calculadora.registros, {"2023-09-14": {"entrada": "09:00", "saida": "17:00"}})

    def test_inserir_horarios_formato_HHmm(self):
        resultado = self.calculadora.inserir_horarios("2023-09-14", "0900", "1730")
        self.assertEqual(resultado, None)
        self.assertEqual(self.calculadora.registros, {"2023-09-14": {"entrada": "09:00", "saida": "17:30"}})

    def test_inserir_intervalo_formato_Hmm(self):
        resultado = self.calculadora.inserir_intervalo("2023-09-14", "60")
        self.assertEqual(resultado, None)
        self.assertEqual(self.calculadora.intervalos, {"2023-09-14": "01:00"})

    def test_inserir_intervalo_formato_HHmm(self):
        resultado = self.calculadora.inserir_intervalo("2023-09-14", "0130")
        self.assertEqual(resultado, None)
        self.assertEqual(self.calculadora.intervalos, {"2023-09-14": "01:30"})

    # Outros testes existentes

if __name__ == "__main__":
    unittest.main()