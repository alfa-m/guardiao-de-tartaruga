texto_inicio = "Bem-vindo ao Guardião de Tartaruguinhas"
texto_opcoes = """
Por favor, selecione uma das opções abaixo ou digite 'sair' para encerrar:
1. Inserir novos ninhos
2. Visualizar relatório completo da semana
3. Consultar estatísticas
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
            print("Inserindo novos ninhos...")
            
        elif opcao_selecionada == '2':
            print("Visualizando relatório completo da semana...")
            
        elif opcao_selecionada == '3':
            print("Consultando estatísticas...")
            
        elif opcao_selecionada.lower() != 'sair':
            print("Opção inválida. Tente novamente.")
    print(texto_final)
    