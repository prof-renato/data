## Exemplo 1
import unittest

class Funcionario():

    def __init__(self, salario, nome, dependentes, altura_cm):
        self.salario = salario
        self.nome = nome
        self.dependentes = dependentes
        self.altura_cm = altura_cm

class FolhaPagamento():

    def calcula_salario_liquido(self, funcionario):
        imposto = funcionario.salario * (funcionario.dependentes * 0.1)
        return funcionario.salario - imposto


class FolhaPagamentoTest(unittest.TestCase):
    # método chamado antes de iniciar os testes
    def setUp(self):
        self.funcionario = Funcionario(3000, "Cláudio André Mergen Taffarel", 1, 171.9)
        self.folha = FolhaPagamento()

    def test_calcula_salario_liquido_controle(self):
        self.assertEqual(2700.0, self.folha.calcula_salario_liquido(self.funcionario))

    def test_calcula_salario_liquido_isento_INSS(self):
        self.funcionario.salario = 1693.72
        self.assertEqual(1524.348, self.folha.calcula_salario_liquido(self.funcionario))

    def test_calcula_salario_liquido_tres_dependentes(self):
        self.funcionario.dependentes = 3
        self.assertEqual(2100.0, self.folha.calcula_salario_liquido(self.funcionario))

unittest.main(argv=[''], verbosity=2, exit=False)
%reset -f

## Exemplo 2
import unittest
import logging
from importlib import reload
reload(logging) 

class Analizador():

    def nome_arquivo_log_valido(self, nome):
        try:
            logging.basicConfig(filename=nome, filemode='a', format='%(asctime)s - %(name)s - %(message)s')
            return True
        except:
            return False


class AnalizadorTest(unittest.TestCase):

    def setUp(self):
        self.analizador = Analizador()

    def test_nome_arquivo_log_valido_letras_maiusculas(self):
        resultado = self.analizador.nome_arquivo_log_valido("log_salvo.LOG")
        self.assertTrue(resultado)

    def test_nome_arquivo_log_valido_letras_minusculas(self):
        resultado = self.analizador.nome_arquivo_log_valido("log_salvo.log")
        self.assertTrue(resultado)

    # método chamado após os testes
    def tearDown(self):
        self.analizador = None

unittest.main(argv=[''], verbosity=2, exit=False)
%reset -f