import unittest
from unittest.mock import patch
import io
from funcoes_analise import (
    total_ninhos, mostra_total_ninhos, lista_ninhos_condional,
    total_ninhos_condicional, mostra_total_ninhos_condicional,
    total_ovos, mostra_total_ovos, total_ovos_condicional,
    mostra_total_ovos_condicional, media_ovos, media_ovos_condicional,
    mostra_media_ovos_condicional
)
from funcoes_ninho import (
    pega_regiao, pega_quantidade_ovos, pega_status, pega_risco,
    pega_dias_para_eclosao, pega_predadores, constroi_dicionario, exibe_ninhos
)
from dados_ninho import lista_de_ninhos as lista_original_ninhos

# Criando uma cópia da lista de ninhos original para que os testes não a modifiquem
lista_de_ninhos_teste = lista_original_ninhos[:]

class TestFuncoesAnalise(unittest.TestCase):

    def setUp(self):
        # Resetar a lista de ninhos para um estado conhecido antes de cada teste
        # Isso é crucial para testes unitários que modificam a lista
        global lista_de_ninhos_teste
        lista_de_ninhos_teste = lista_original_ninhos[:]


    def test_total_ninhos(self):
        self.assertEqual(total_ninhos(lista_de_ninhos_teste), 11) # Atualizado para 11 após correção da duplicação

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos(self, mock_stdout):
        mostra_total_ninhos(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ninhos registrados: 11')
        
        mostra_total_ninhos([])
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ninhos registrados: 11\nNão há nenhum ninho registrado.')


    def test_lista_ninhos_condional(self):
        ninhos_predadores = lista_ninhos_condional(lista_de_ninhos_teste, 'predadores', 'true')
        self.assertEqual(len(ninhos_predadores), 5) # ninho_2, ninho_5, ninho_7, ninho_9, ninho_11

        ninhos_eclosao = lista_ninhos_condional(lista_de_ninhos_teste, 'eclosão', 'sim')
        self.assertEqual(len(ninhos_eclosao), 4) # ninho_2, ninho_4, ninho_5, ninho_9

        ninhos_regiao = lista_ninhos_condional(lista_de_ninhos_teste, 'regiao', 'Praia Central')
        self.assertEqual(len(ninhos_regiao), 2) # ninho_2, ninho_4


    def test_total_ninhos_condicional(self):
        self.assertEqual(total_ninhos_condicional(lista_de_ninhos_teste, 'regiao', 'Praia Norte'), 2)
        self.assertEqual(total_ninhos_condicional(lista_de_ninhos_teste, 'predadores', 'true'), 5)
        self.assertEqual(total_ninhos_condicional(lista_de_ninhos_teste, 'eclosão', 'sim'), 4)
        self.assertEqual(total_ninhos_condicional(lista_de_ninhos_teste, 'status', 'inexistente'), -1) # Teste de valor inválido
        self.assertEqual(total_ninhos_condicional(lista_de_ninhos_teste, 'condicao_invalida', 'valor'), -1) # Teste de condição inválida

    @patch('builtins.input', side_effect=['regiao', 'praia norte'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_regiao(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ninhos para a condição "regiao" igual a "Praia Norte": 2')

    @patch('builtins.input', side_effect=['predadores', 'true'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_predadores_true(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ninhos com presença de predadores: 5')

    @patch('builtins.input', side_effect=['eclosão', 'sim'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_eclosao_sim(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ninhos próximos a eclosão: 4')

    @patch('builtins.input', side_effect=['regiao', 'valor_invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_valor_invalido(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Valor de condição inválido.')

    @patch('builtins.input', side_effect=['predadores', 'invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_predadores_invalido(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Valor de condição inválido. Use 'true' ou 'false'.")

    @patch('builtins.input', side_effect=['eclosão', 'invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_eclosao_invalido(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Valor de condição inválido. Use 'sim' ou 'não'.")

    @patch('builtins.input', side_effect=['condicao_invalida'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ninhos_condicional_condicao_invalida(self, mock_stdout, mock_input):
        mostra_total_ninhos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")


    def test_total_ovos(self):
        self.assertEqual(total_ovos(lista_de_ninhos_teste), 936) # Calculado manualmente a soma dos ovos

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos(self, mock_stdout):
        mostra_total_ovos(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ovos registrados: 936')
        
        mostra_total_ovos([])
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ovos registrados: 936\nNão há ovos registrados.')


    def test_total_ovos_condicional(self):
        self.assertEqual(total_ovos_condicional(lista_de_ninhos_teste, 'regiao', 'Praia Norte'), 162)
        self.assertEqual(total_ovos_condicional(lista_de_ninhos_teste, 'predadores', 'true'), 364)
        self.assertEqual(total_ovos_condicional(lista_de_ninhos_teste, 'eclosão', 'sim'), 324)
        self.assertEqual(total_ovos_condicional(lista_de_ninhos_teste, 'status', 'inexistente'), -1)
        self.assertEqual(total_ovos_condicional(lista_de_ninhos_teste, 'condicao_invalida', 'valor'), -1)

    @patch('builtins.input', side_effect=['regiao', 'praia norte'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos_condicional_regiao(self, mock_stdout, mock_input):
        mostra_total_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ovos para a condição "regiao" igual a "Praia Norte": 162')
    
    @patch('builtins.input', side_effect=['predadores', 'true'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos_condicional_predadores_true(self, mock_stdout, mock_input):
        mostra_total_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ovos com presença de predadores: 364')

    @patch('builtins.input', side_effect=['eclosão', 'sim'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos_condicional_eclosao_sim(self, mock_stdout, mock_input):
        mostra_total_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Total de ovos próximos a eclosão: 324')

    @patch('builtins.input', side_effect=['predadores', 'invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos_condicional_predadores_invalido(self, mock_stdout, mock_input):
        mostra_total_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Valor de condição inválido. Use 'true' ou 'false'.")
    
    @patch('builtins.input', side_effect=['eclosão', 'invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos_condicional_eclosao_invalido(self, mock_stdout, mock_input):
        mostra_total_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Valor de condição inválido. Use 'sim' ou 'não'.")

    @patch('builtins.input', side_effect=['condicao_invalida'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_total_ovos_condicional_condicao_invalida(self, mock_stdout, mock_input):
        mostra_total_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")


    def test_media_ovos(self):
        self.assertAlmostEqual(media_ovos(lista_de_ninhos_teste), 936 / 11, places=2)
        self.assertEqual(media_ovos([]), 0)

    def test_media_ovos_condicional(self):
        self.assertAlmostEqual(media_ovos_condicional(lista_de_ninhos_teste, 'regiao', 'Praia Norte'), 162 / 2, places=2)
        self.assertAlmostEqual(media_ovos_condicional(lista_de_ninhos_teste, 'predadores', 'true'), 364 / 5, places=2)
        self.assertAlmostEqual(media_ovos_condicional(lista_de_ninhos_teste, 'eclosão', 'sim'), 324 / 4, places=2)
        self.assertEqual(media_ovos_condicional(lista_de_ninhos_teste, 'status', 'inexistente'), -1)
        self.assertEqual(media_ovos_condicional(lista_de_ninhos_teste, 'condicao_invalida', 'valor'), -1)

    @patch('builtins.input', side_effect=['regiao', 'praia norte'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_media_ovos_condicional_regiao(self, mock_stdout, mock_input):
        mostra_media_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Média de ovos para a condição "regiao" igual a "Praia Norte": 81.00')
    
    @patch('builtins.input', side_effect=['predadores', 'true'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_media_ovos_condicional_predadores_true(self, mock_stdout, mock_input):
        mostra_media_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Média de ovos com presença de predadores: 72.80')

    @patch('builtins.input', side_effect=['eclosão', 'sim'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_media_ovos_condicional_eclosao_sim(self, mock_stdout, mock_input):
        mostra_media_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Média de ovos próximos a eclosão: 81.00')

    @patch('builtins.input', side_effect=['predadores', 'invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_media_ovos_condicional_predadores_invalido(self, mock_stdout, mock_input):
        mostra_media_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Valor de condição inválido. Use 'true' ou 'false'.")
    
    @patch('builtins.input', side_effect=['eclosão', 'invalido'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_media_ovos_condicional_eclosao_invalido(self, mock_stdout, mock_input):
        mostra_media_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Valor de condição inválido. Use 'sim' ou 'não'.")

    @patch('builtins.input', side_effect=['condicao_invalida'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostra_media_ovos_condicional_condicao_invalida(self, mock_stdout, mock_input):
        mostra_media_ovos_condicional(lista_de_ninhos_teste)
        self.assertEqual(mock_stdout.getvalue().strip(), "Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")


class TestFuncoesNinho(unittest.TestCase):

    # Usa patch para isolar a lista_de_ninhos de dados_ninho.py
    # Isso permite que os testes de constroi_dicionario adicionem ninhos sem afetar outros testes
    @patch('funcoes_ninho.lista_de_ninhos', [])
    def test_constroi_dicionario_sucesso(self, mock_lista_de_ninhos):
        # Simula as entradas do usuário
        with patch('builtins.input', side_effect=[
            'Praia Teste',   # regiao
            '99',            # quantidade_ovos
            'intacto',       # status
            'estável',       # risco
            '15',            # dias_para_eclosao
            'não'            # predadores
        ]):
            ninho = constroi_dicionario()
            self.assertIsNotNone(ninho)
            self.assertEqual(ninho['regiao'], 'Praia Teste')
            self.assertEqual(ninho['quantidade_ovos'], 99)
            self.assertEqual(ninho['status'], 'intacto')
            self.assertEqual(ninho['risco'], 'estável')
            self.assertEqual(ninho['dias_para_eclosao'], 15)
            self.assertFalse(ninho['predadores'])
            self.assertEqual(len(mock_lista_de_ninhos), 1)
            self.assertEqual(mock_lista_de_ninhos[0], ninho)

    @patch('funcoes_ninho.lista_de_ninhos', [])
    def test_constroi_dicionario_predadores_sim(self, mock_lista_de_ninhos):
        with patch('builtins.input', side_effect=[
            'Praia Outra',
            '50',
            'ameaçado',
            'crítico',
            '1',
            'sim' # predadores
        ]):
            ninho = constroi_dicionario()
            self.assertIsNotNone(ninho)
            self.assertTrue(ninho['predadores'])
            self.assertEqual(len(mock_lista_de_ninhos), 1)

    @patch('funcoes_ninho.lista_de_ninhos', [])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_constroi_dicionario_predadores_entrada_invalida(self, mock_stdout, mock_lista_de_ninhos):
        with patch('builtins.input', side_effect=[
            'Praia Inválida',
            '10',
            'intacto',
            'estável',
            '20',
            'abc', # Entrada inválida para predadores
            'não'  # Entrada válida na segunda tentativa
        ]):
            ninho = constroi_dicionario()
            self.assertIsNotNone(ninho)
            self.assertIn("Erro: Resposta inválida. Digite 'sim' ou 'não'.", mock_stdout.getvalue())
            self.assertFalse(ninho['predadores'])
            self.assertEqual(len(mock_lista_de_ninhos), 1)

    @patch('funcoes_ninho.lista_de_ninhos', [])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_constroi_dicionario_quantidade_ovos_invalida(self, mock_stdout, mock_lista_de_ninhos):
        with patch('builtins.input', side_effect=[
            'Praia Erro',
            '-5', # Entrada inválida
            '10', # Entrada válida
            'intacto',
            'estável',
            '10',
            'não'
        ]):
            ninho = constroi_dicionario()
            self.assertIsNotNone(ninho)
            self.assertIn("Erro: A quantidade de ovos deve ser um número inteiro positivo.", mock_stdout.getvalue())
            self.assertEqual(ninho['quantidade_ovos'], 10)
            self.assertEqual(len(mock_lista_de_ninhos), 1)

    @patch('funcoes_ninho.lista_de_ninhos', lista_original_ninhos[:]) # Usa a lista original para este teste
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exibe_ninhos(self, mock_stdout):
        exibe_ninhos()
        output = mock_stdout.getvalue()
        self.assertIn("Ninho 1:", output)
        self.assertIn("regiao: Praia Norte", output)
        self.assertIn("Ninho 11:", output)
        self.assertIn("regiao: Praia Oeste", output)
        self.assertIn("predadores: True", output) # Verificar a correção de predadores na saída

    @patch('funcoes_ninho.lista_de_ninhos', [])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exibe_ninhos_vazia(self, mock_stdout):
        exibe_ninhos()
        self.assertEqual(mock_stdout.getvalue().strip(), "Nenhum ninho registrado.")

    @patch('builtins.input', side_effect=['Praia Apenas Letras'])
    def test_pega_regiao_valido(self):
        self.assertEqual(pega_regiao(), 'Praia Apenas Letras')

    @patch('builtins.input', side_effect=['Praia123', 'Praia Valida'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pega_regiao_invalido(self, mock_stdout):
        self.assertEqual(pega_regiao(), 'Praia Valida')
        self.assertIn("Erro: A região deve conter apenas letras e espaços.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['100'])
    def test_pega_quantidade_ovos_valido(self):
        self.assertEqual(pega_quantidade_ovos(), 100)

    @patch('builtins.input', side_effect=['abc', '-10', '50'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pega_quantidade_ovos_invalido(self, mock_stdout):
        self.assertEqual(pega_quantidade_ovos(), 50)
        self.assertIn("Erro: A quantidade de ovos deve ser um número inteiro positivo.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['intacto'])
    def test_pega_status_valido(self):
        self.assertEqual(pega_status(), 'intacto')

    @patch('builtins.input', side_effect=['errado', 'danificado'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pega_status_invalido(self, mock_stdout):
        self.assertEqual(pega_status(), 'danificado')
        self.assertIn("Erro: O status deve ser 'intacto', 'ameaçado' ou 'danificado'.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['estável'])
    def test_pega_risco_valido(self):
        self.assertEqual(pega_risco(), 'estável')

    @patch('builtins.input', side_effect=['errado', 'crítico'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pega_risco_invalido(self, mock_stdout):
        self.assertEqual(pega_risco(), 'crítico')
        self.assertIn("Erro: O risco deve ser 'estável', 'sob observação' ou 'crítico'.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['7'])
    def test_pega_dias_para_eclosao_valido(self):
        self.assertEqual(pega_dias_para_eclosao(), 7)

    @patch('builtins.input', side_effect=['abc', '-3', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pega_dias_para_eclosao_invalido(self, mock_stdout):
        self.assertEqual(pega_dias_para_eclosao(), 5)
        self.assertIn("Erro: Os dias restantes para a eclosão devem ser um número inteiro positivo.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['sim'])
    def test_pega_predadores_sim(self):
        self.assertTrue(pega_predadores())

    @patch('builtins.input', side_effect=['não'])
    def test_pega_predadores_nao(self):
        self.assertFalse(pega_predadores())

    @patch('builtins.input', side_effect=['talvez', 'sim'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pega_predadores_invalido(self, mock_stdout):
        self.assertTrue(pega_predadores())
        self.assertIn("Erro: Resposta inválida. Digite 'sim' ou 'não'.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)