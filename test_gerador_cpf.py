import unittest
from gerador_cpf import gera_cpf, calcula_digito

class TestGeradorCPF(unittest.TestCase):
    def test_calcula_digito(self):
        # Testes para os cálculos dos dígitos verificadores
        self.assertEqual(calcula_digito('123456789', 10), 0)
        self.assertEqual(calcula_digito('987654321', 11), 0)
    
    def test_gera_cpf(self):
        # Teste para verificar se o CPF gerado é válido e não contém sequências ou repetições
        for _ in range(1000):  # Testa 1000 vezes para garantir a aleatoriedade
            cpf = gera_cpf()
            self.assertEqual(len(cpf), 11)
            self.assertTrue(cpf.isdigit())
            self.assertNotIn(cpf[:9], ['123456789', '987654321'])
            self.assertFalse(all(n == cpf[0] for n in cpf[:9]))

if __name__ == '__main__':
    unittest.main()
