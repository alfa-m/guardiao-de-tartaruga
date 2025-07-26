import dados_ninho
import funcoes_ninho
import funcoes_analise

ninhos = dados_ninho.lista_de_ninhos

texto_inicio = "Bem-vindo ao Guardião de Tartaruguinhas"
texto_opcoes = """
------------------------------------ Menu Principal ------------------------------------
Por favor, selecione uma das opções abaixo ou digite 'sair' para encerrar:
1. Inserir novos ninhos
2. Visualizar relatório completo da semana
3. Consultar estatísticas
----------------------------------------------------------------------------------------
"""
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
texto_final = """
Obrigado por usar o Guardião de Tartaruguinhas!
Encerrando o programa.
"""

def mostra_menu():
    print(texto_inicio)
    opcao_selecionada = ""
    while opcao_selecionada.lower() != 'sair':
        print(texto_opcoes)
        opcao_selecionada = input("Digite sua opção: ")
        
        if opcao_selecionada == '1':
            inserir_ninhos()
            
        elif opcao_selecionada == '2':
            exibir_ninhos()
            
        elif opcao_selecionada == '3':
            consultar_estatisticas()
            
        elif opcao_selecionada.lower() != 'sair':
            print("Opção inválida. Tente novamente.")
    print(texto_final)
    
def inserir_ninhos():
    print("Você escolheu inserir um novo ninho.")
    print("Construindo dicionário do ninho...")
    funcoes_ninho.constroi_dicionario()
    opcao_continuar = input("Deseja inserir outro ninho? (sim/não): ")
    if opcao_continuar.lower() == 'sim':
        inserir_ninhos()
    elif opcao_continuar.lower() == 'não':
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Voltando ao menu principal...")

def exibir_ninhos():
    print("Você escolheu visualizar o relatório completo da semana.")
    print("Exibindo ninhos registrados...")
    funcoes_ninho.exibe_ninhos()
    opcao_continuar = input("Deseja consultar o relatório novamente? (sim/não): ")
    if opcao_continuar.lower() == 'sim':
        consultar_estatisticas()
    elif opcao_continuar.lower() == 'não':
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Voltando ao menu principal...")

def consultar_estatisticas():
    print("Você escolheu consultar estatísticas.")
    print("Consultando estatísticas...")
    opcao_estatistica = ""
    while opcao_estatistica != 'voltar':
        print(texto_opcoes_estatisticas)
        opcao_estatistica = input("Digite sua opção: ")
        
        if opcao_estatistica == '1':
            print("Você escolheu ver a quantidade total de ninhos")
            funcoes_analise.mostra_total_ninhos(ninhos)
            
        elif opcao_estatistica == '2':
            print("Você escolheu ver a média de ovos por ninho com risco 'estável'")
            media = funcoes_analise.media_ovos_condicional(ninhos, 'risco', 'estável')
            print(f'Média de ovos por ninho com risco "estável": {media}')
            
        elif opcao_estatistica == '3':
            print("Você escolheu ver a quantidade de ninhos prestes a eclodir (dias <= 5)")
            total = funcoes_analise.total_ninhos_condicional(ninhos, 'eclosão', 'sim')
            print(f'Quantidade de ninhos próximos a eclosão: {total}')
            
        elif opcao_estatistica == '4':
            print("Região com maior quantidade de ninhos sob risco 'crítico':")
            
        elif opcao_estatistica == '5':
            print("Quantidade de ninhos com presença de predadores e com status 'danificado':")
            
        elif opcao_estatistica.lower() != 'voltar':
            print("Opção inválida. Tente novamente.")
    print("Voltando ao menu principal...")