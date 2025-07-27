## Arquivo menu.py
## Sobre o arquivo:
### Contém as funções de menu e interação com o usuário

## Import dos módulos necessários para a execução do menu
# Importa o módulo com dados iniciais dos ninhos
import dados_ninho
# Importa o módulo com funções relacionadas a criação de ninhos
import funcoes_ninho
# Importa o módulo com funções de análise dos dados dos ninhos
import funcoes_analise
# Importa o módulo com funções complementares para manipulação de dados
import funcoes_complementares

# Salva os dados iniciais de ninhos, contidos no módulo dados_ninho, em uma variável
ninhos = dados_ninho.lista_de_ninhos

## Criação de variáveis de texto para o menu
# Texto de boas-vindas
texto_inicio = "Bem-vindo ao Guardião de Tartaruguinhas"
# Texto de opções do menu principal
texto_opcoes = """
------------------------------------ Menu Principal ------------------------------------
Por favor, selecione uma das opções abaixo ou digite 'sair' para encerrar:
1. Inserir novos ninhos
2. Visualizar relatório completo da semana
3. Consultar estatísticas
----------------------------------------------------------------------------------------
"""
# Texto de opções para estatísticas
texto_opcoes_estatisticas = """
------------------------------------- Estatísticas -------------------------------------
Escolha uma das estatísticas abaixo ou digite 'voltar' para retornar ao menu principal:
1. Quantidade de ninhos total
2. Média de ovos por ninho com risco "estável"
3. Quantidade de ninhos prestes a eclodir (dias <= 5)
4. Região com maior quantidade de ninhos sob risco "crítico"
5. Quantidade de ninhos com presença de predadores e com status "danificado"
----------------------------------------------------------------------------------------
"""
# Texto de encerramento do programa
texto_final = """
Obrigado por usar o Guardião de Tartaruguinhas!
Encerrando o programa.
"""

## Criação de funções para o menu
# Função que exibe o menu e permite ao usuário interagir com as opções disponíveis
def mostra_menu():
    # Mostra o texto de boas-vindas
    print(texto_inicio)
    # Cria a variável para armazenar a opção selecionada pelo usuário
    opcao_selecionada = ""
    # Inicia um loop para exibir o menu até que o usuário escolha "sair"
    while opcao_selecionada.lower() != 'sair':
        # Exibe as opções do menu principal
        print(texto_opcoes)
        # Solicita ao usuário que digite uma opção
        opcao_selecionada = input("Digite sua opção: ")
        
        ## Verifica a opção selecionada e executa a ação correspondente
        # Se o usuário escolher a opção 1, chama a função para inserir ninhos
        if opcao_selecionada == '1':
            inserir_ninhos()
        
        # Se o usuário escolher a opção 2, chama a função para exibir ninhos
        elif opcao_selecionada == '2':
            exibir_ninhos()
        
        # Se o usuário escolher a opção 3, chama a função para consultar estatísticas
        elif opcao_selecionada == '3':
            consultar_estatisticas()
        
        # Se o usuário escolher qualquer outra opção que não seja "sair", exibe uma mensagem de erro
        elif opcao_selecionada.lower() != 'sair':
            # Exibe uma mensagem de erro para opção inválida
            print("Opção inválida. Tente novamente.")
    # Exibe o texto de encerramento do programa quando o usuário escolher "sair"
    print(texto_final)

# Funções para inserir ninhos
def inserir_ninhos():
    # Exibe uma mensagem informando a opção escolhida pelo usuário
    print("Você escolheu inserir um novo ninho.")
    print("Construindo dicionário do ninho...")
    # Chama a função para construir o dicionário do ninho
    funcoes_ninho.constroi_dicionario()
    # Verifica se o usuário deseja inserir outro ninho
    opcao_continuar = input("Deseja inserir outro ninho? (sim/não): ")
    # Se o usuário escolher "sim", chama a função para inserir ninhos novamente
    if opcao_continuar.lower() == 'sim':
        inserir_ninhos()
    # Se o usuário escolher "não", exibe uma mensagem de retorno ao menu principal
    elif opcao_continuar.lower() == 'não':
        print("Voltando ao menu principal...")
    # Se o usuário escolher qualquer outra opção, exibe uma mensagem de erro
    else:
        print("Opção inválida. Voltando ao menu principal...")

# Função para exibir os ninhos registrados
def exibir_ninhos():
    # Exibe uma mensagem informando a opção escolhida pelo usuário
    print("Você escolheu visualizar o relatório completo da semana.")
    print("Exibindo ninhos registrados...")
    # Chama a função para exibir os ninhos
    funcoes_ninho.exibe_ninhos()
    # Verifica se o usuário deseja consultar o relatório novamente
    opcao_continuar = input("Deseja consultar o relatório novamente? (sim/não): ")
    # Se o usuário escolher "sim", chama a função para exibir ninhos novamente
    if opcao_continuar.lower() == 'sim':
        exibir_ninhos()
    # Se o usuário escolher "não", exibe uma mensagem de retorno ao menu principal
    elif opcao_continuar.lower() == 'não':
        print("Voltando ao menu principal...")
    # Se o usuário escolher qualquer outra opção, exibe uma mensagem de erro
    else:
        print("Opção inválida. Voltando ao menu principal...")

# Função para consultar estatísticas
def consultar_estatisticas():
    # Exibe uma mensagem informando a opção escolhida pelo usuário
    print("Você escolheu consultar estatísticas.")
    print("Consultando estatísticas...")
    # Cria uma variável para armazenar a opção de estatística selecionada pelo usuário
    opcao_estatistica = ""
    # Inicia um loop para exibir as opções de estatísticas até que o usuário escolha "voltar"
    while opcao_estatistica != 'voltar':
        # Exibe as opções de estatísticas
        print(texto_opcoes_estatisticas)
        # Solicita ao usuário que digite uma opção de estatística
        opcao_estatistica = input("Digite sua opção: ")
        
        ## Verifica a opção selecionada e executa a ação correspondente
        # Se o usuário escolher a opção 1, exibe a quantidade total de ninhos
        if opcao_estatistica == '1':
            # Exibe uma mensagem informando a opção escolhida pelo usuário
            print("Você escolheu ver a quantidade total de ninhos")
            # Chama a função para exibir o total de ninhos
            funcoes_analise.mostra_total_ninhos(ninhos)
        
        # Se o usuário escolher a opção 2, exibe a média de ovos por ninho com risco "estável"
        elif opcao_estatistica == '2':
            # Exibe uma mensagem informando a opção escolhida pelo usuário
            print("Você escolheu ver a média de ovos por ninho com risco 'estável'")
            # Chama a função para calcular a média de ovos com risco "estável" e salva o resultado em uma variável
            media = funcoes_analise.media_ovos_condicional(ninhos, 'risco', 'estável')
            # Exibe a média de ovos por ninho com risco "estável"
            print(f'Média de ovos por ninho com risco "estável": {media}')
        
        # Se o usuário escolher a opção 3, exibe a quantidade de ninhos prestes a eclodir
        elif opcao_estatistica == '3':
            # Exibe uma mensagem informando a opção escolhida pelo usuário
            print("Você escolheu ver a quantidade de ninhos prestes a eclodir (dias <= 5)")
            # Chama a função para calcular o total de ninhos próximos a eclosão e salva o resultado em uma variável
            total = funcoes_analise.total_ninhos_condicional(ninhos, 'eclosão', 'sim')
            # Exibe a quantidade de ninhos próximos a eclosão
            print(f'Quantidade de ninhos próximos a eclosão: {total}')
        
        # Se o usuário escolher a opção 4, exibe a região com maior quantidade de ninhos sob risco "crítico"
        elif opcao_estatistica == '4':
            # Exibe uma mensagem informando a opção escolhida pelo usuário
            print("Você escolheu ver a região com maior quantidade de ninhos sob risco 'crítico'")
            # Chama a função para filtrar os ninhos com risco "crítico" e salva o resultado em uma variável
            ninhos_criticos = funcoes_analise.lista_ninhos_condional(ninhos, 'risco', 'crítico')
            # Obtém os valores únicos de regiões dos ninhos críticos usando a função de valores únicos e salva o resultado em uma variável
            valores_unicos_regioes = funcoes_complementares.valores_unicos_chave(ninhos_criticos, 'regiao')
            # Inicializa variável para armazenar a região com maior quantidade de ninhos críticos
            regiao_mais_critico = ""
            # Inicializa variável para armazenar a quantidade máxima de ninhos críticos
            maior = 0
            # Itera sobre as regiões únicas para encontrar a região com maior quantidade de ninhos críticos
            for regiao in valores_unicos_regioes:
                # Chama a função para contar a quantidade de ninhos críticos pela região atual
                quantidade_ninhos = funcoes_analise.total_ninhos_condicional(ninhos_criticos, 'regiao', regiao)
                # Se a quantidade de ninhos críticos na região atual for maior que a quantidade máxima encontrada até agora, salva a região e a quantidade
                if quantidade_ninhos > maior:
                    maior = quantidade_ninhos
                    regiao_mais_critico = regiao
            # Exibe a região com maior quantidade de ninhos críticos
            print(f'Região com maior quantidade de ninhos sob risco "crítico": {regiao_mais_critico}')
        
        # Se o usuário escolher a opção 5, exibe a quantidade de ninhos com presença de predadores e com status "danificado"
        elif opcao_estatistica == '5':
            # Exibe uma mensagem informando a opção escolhida pelo usuário
            print("Você escolheu ver a quantidade de ninhos com presença de predadores e com status 'danificado'")
            # Chama a função para filtrar os ninhos com status "danificado" e salva o resultado em uma variável
            ninhos_danificados = funcoes_analise.lista_ninhos_condional(ninhos, 'status', 'danificado')
            # Chama a função para contar a quantidade de ninhos com presença de predadores e status "danificado" e salva o resultado em uma variável
            total = funcoes_analise.total_ninhos_condicional(ninhos_danificados, 'predadores', 'true')
            # Exibe o total de ninhos com presença de predadores e status "danificado"
            print(f'Quantidade de ninhos com presença de predadores e status "danificado": {total}')
        
        # Se o usuário escolher qualquer outra opção que não seja "voltar", exibe uma mensagem de erro
        elif opcao_estatistica.lower() != 'voltar':
            print("Opção inválida. Tente novamente.")
    # Exibe uma mensagem de retorno ao menu principal quando o usuário escolher "voltar"
    print("Voltando ao menu principal...")
