## Arquivo funcoes_analise.py
## Sobre o arquivo:
### Contém as funções relacionadas às análises estatísticas

# Importa o módulo com as funções complementares
import funcoes_complementares

## Criação de funções para contagem de ninhos
# Função que conta a quantidade de ninhos
def total_ninhos(lista_de_ninhos):
    return len(lista_de_ninhos)

# Função que mostra a quantidade de ninhos
def mostra_total_ninhos(lista_de_ninhos):
    # Verifica a quantidade de ninhos e salva em uma variável
    total = total_ninhos(lista_de_ninhos)
    ## Verifica se tem ninhos registrados
    # Se houverem, mostra a quantidade de ninhos
    if total != 0:
        print('Total de ninhos registrados:', total)
    # Senão, informa que não há ninhos salvos
    else:
        print("Não há nenhum ninho registrado.")


## Criação de funções para contagem de ninhos condicionais
# Função que cria uma lista de ninhos que correnspondem às condições inseridas
def lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao):
    ## Verifica o tipo de condição
    # Se a condição for preadores e o valor da condição for true, faz a lista para ninhos com 'predadores' == True
    if condicao == 'predadores' and valor_condicao == 'true':
        return [ninho for ninho in lista_de_ninhos if ninho['predadores'] == True]
    # Se a condição for preadores e o valor da condição for false, faz a lista para ninhos com 'predadores' == False
    elif condicao == 'predadores' and valor_condicao == 'false':
        return [ninho for ninho in lista_de_ninhos if ninho['predadores'] == False]
    # Se a condição for eclosão e o valor for sim, faz a lista para ninhos com 'dias_para_eclosao' <= 5
    elif condicao == 'eclosão' and valor_condicao == 'sim':
        return [ninho for ninho in lista_de_ninhos if ninho['dias_para_eclosao'] <= 5]
    # Se a condição for eclosão e o valor for não, faz a lista para ninhos com 'dias_para_eclosao' > 5
    elif condicao == 'eclosão' and valor_condicao == 'não':
        return [ninho for ninho in lista_de_ninhos if ninho['dias_para_eclosao'] > 5]
    # Se forem outras condições, faz a lista para ninhos com essa condição
    else:
        return [ninho for ninho in lista_de_ninhos if ninho[condicao] == valor_condicao]

# Função que conta a quantidade de ninhos que correnspondem às condições inseridas
def total_ninhos_condicional(lista_de_ninhos, condicao, valor_condicao):
    ## Verifica o tipo de condição
    # Se a condição for eclosão, chama a função lista_ninhos_condicao
    if condicao == 'eclosão':
        lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
        return total_ninhos(lista_ninhos_condicao)
    # Se o tipo de condição for regiao, status, risco e predadores, verifica a lista de valores unicos para essa chave
    elif condicao in ['regiao', 'status', 'risco', 'predadores']:
        valores_unicos_condicao = funcoes_complementares.valores_unicos_chave(lista_de_ninhos, condicao)
        ## Verifica se o valor de condição passado está na lista de valores únicos
        # Se o valor estiver na lista, chama a função lista_ninhos_condicao
        if valor_condicao in valores_unicos_condicao:
            lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
            return total_ninhos(lista_ninhos_condicao)
        # Senão, retorna um valor negativo
        else:
            return -1
    # Se a condição não corrsponder a nenhuma das opções válidas, retornar um valor negativo
    else:
        return -1

# Função que mostra a quantidade de ninhos que correnspondem às condições inseridas
def mostra_total_ninhos_condicional(lista_de_ninhos):
    # Solicita a condição para o usuário, padroniza a entrada para letras minúsculas
    condicao = input("Digite a condição (regiao, status, risco, eclosão, predadores): ").lower()
    ## Verifica a entrada do usuário
    # Se a entrada for regiao, status ou risco, pede o valor da condição e padroniza para letras minúsculas
    if condicao in ['regiao', 'status', 'risco']:
        valor_condicao = input(f'Digite o valor para a condição "{condicao}": ').lower()
        # Se a condição for regiao, deixa o valor de entrada com a primeira letra de cada palavra maiúscula
        if condicao == 'regiao':
            valor_condicao = valor_condicao.title()
        # Realiza busca para a condição selecionada e o valor de entrada padronizado
        total = total_ninhos_condicional(lista_de_ninhos, condicao, valor_condicao)
        ## Verifica o valor retornado por total_ninhos_condicional
        # Se o valor não for negativo, mostra a quantidade de ninhos
        if total != -1:
            print(f'Total de ninhos para a condição "{condicao}" igual a "{valor_condicao}":', total)
        # Se for um valor negativo, informa que o valor foi inválido
        else:
            print("Valor de condição inválido.")

    # Se a condição for predadores, define os tipos de valor desejados
    elif condicao == 'predadores':
        # Solicita o valor para o usuário
        valor_condicao = input('Digite o valor para a condição "predadores" (true/false): ')
        ## Verifica o valor inserido pelo usuário
        # Se o valor for true ou false, o código faz mais validações
        if valor_condicao in ['true', 'false']:
            # Passa as condições para total_ninhos_condicional
            total = total_ninhos_condicional(lista_de_ninhos, 'predadores', valor_condicao)
            ## Verifica o valor retornado por total_ninhos_condicional
            # Se o valor não for negativo e a condição for true, mostra a mensagem de ninhos com presença de predadores
            if total != -1 and valor_condicao == 'true':
                print('Total de ninhos com presença de predadores:', total)
            # Se o valor não for negativo e a condição for false, mostra a mensagem de ninhos sem presença de predadores
            elif total != -1 and valor_condicao == 'false':
                print('Total de ninhos sem presença de predadores:', total)
            # Se for outra opção, informa que o valor inserido não é válido
            else:
                print("Valor de condição inválido.")
        # Se não for, informa que o valor inserido não é válido
        else:
            print("Valor de condição inválido. Use 'true' ou 'false'.")
        
    # Se a condição for eclosão, define os tipos de valor desejados
    elif condicao == 'eclosão':
        # Solicita o valor para o usuário
        valor_condicao = input('Digite o valor para a condição "eclosão" (sim/não): ').lower()
        ## Verifica o valor inserido pelo usuário
        # Se o valor for sim ou não, o código faz mais validações
        if valor_condicao in ['sim', 'não']:
            # Passa as condições para a função total_ninhos_condicional
            total = total_ninhos_condicional(lista_de_ninhos, 'eclosão', valor_condicao)
            ## Verifica o valor retornado por total_ninhos_condicional
            # Se o valor não for negativo e a condição for sim, mostra a quantidade de ninhos próximos a eclosão
            if total != -1 and valor_condicao == 'sim':
                print('Total de ninhos próximos a eclosão:', total)
            # Se o valor não for negativo e a condição for não, mostra a quantidade de ninhos não próximos a eclosão
            elif total != -1 and valor_condicao == 'não':
                print('Total de ninhos não próximos a eclosão:', total)
            # Se for outra opção, informa que o valor inserido não é válido
            else:
                print("Valor de condição inválido.")
        # Se não for, informa que o valor inserido não é válido
        else:
            print("Valor de condição inválido. Use 'sim' ou 'não'.")
    # Se não for, informa que a condição não é válida
    else:
        print("Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")

## Realiza as mesmas funções de ninho estabelecidas acima, porém considerando a quantidade de ovos
def total_ovos(lista_de_ninhos):
    return sum(ninho['quantidade_ovos'] for ninho in lista_de_ninhos if 'quantidade_ovos' in ninho)

def mostra_total_ovos(lista_de_ninhos):
    total = total_ovos(lista_de_ninhos)
    if total != 0:
        print('Total de ovos registrados:', total)
    else:
        print("Não há ovos registrados.")

def total_ovos_condicional(lista_de_ninhos, condicao, valor_condicao):
    if condicao == 'eclosão':
        lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
        return total_ovos(lista_ninhos_condicao)
    elif condicao in ['regiao', 'status', 'risco', 'predadores']:
        valores_unicos_condicao = funcoes_complementares.valores_unicos_chave(lista_de_ninhos, condicao)
        if valor_condicao in valores_unicos_condicao:
            lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
            return total_ovos(lista_ninhos_condicao)
        else:
            return -1
    else:
        return -1

def mostra_total_ovos_condicional(lista_de_ninhos):
    condicao = input("Digite a condição (regiao, status, risco, eclosão, predadores): ").lower()
    if condicao in ['regiao', 'status', 'risco', 'predadores']:
        valor_condicao = input(f'Digite o valor para a condição "{condicao}": ').lower()
        if condicao == 'regiao':
            valor_condicao = valor_condicao.title()
        total = total_ovos_condicional(lista_de_ninhos, condicao, valor_condicao)
        if total != -1:
            print(f'Total de ovos para a condição "{condicao}" igual a "{valor_condicao}":', total)
        else:
            print("Valor de condição inválido.")
    elif condicao == 'predadores':
        valor_condicao = input('Digite o valor para a condição "predadores" (true/false): ')
        if valor_condicao in ['true', 'false']:
            total = total_ovos_condicional(lista_de_ninhos, 'predadores', valor_condicao)
            if total != -1 and valor_condicao == 'true':
                print('Total de ovos com presença de predadores:', total)
            elif total != -1 and valor_condicao == 'false':
                print('Total de ovos sem presença de predadores:', total)
            else:
                print("Valor de condição inválido.")
        else:
            print("Valor de condição inválido. Use 'true' ou 'false'.")
    elif condicao == 'eclosão':
        valor_condicao = input('Digite o valor para a condição "eclosão" (sim/não): ').lower()
        if valor_condicao in ['sim', 'não']:
            total = total_ovos_condicional(lista_de_ninhos, 'eclosão', valor_condicao)
            if total != -1 and valor_condicao == 'sim':
                print(f'Total de ovos próximos a eclosão:', total)
            elif total != -1 and valor_condicao == 'não':
                print(f'Total de ovos não próximos a eclosão:', total)
            else:
                print("Valor de condição inválido.")
        else:
            print("Valor de condição inválido. Use 'sim' ou 'não'.")
    else:
        print("Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")

## Realiza as mesmas funções de ovos estabelecidas acima, porém considerando a média de ovos
def media_ovos(lista_de_ninhos):
    if len(lista_de_ninhos) != 0:
        total = total_ovos(lista_de_ninhos)
        media = total / len(lista_de_ninhos)
        return media
    else:
        return 0

def media_ovos_condicional(lista_de_ninhos, condicao, valor_condicao):
    if condicao == 'eclosão':
        lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
        return media_ovos(lista_ninhos_condicao)
    elif condicao in ['regiao', 'status', 'risco', 'predadores']:
        valores_unicos_condicao = funcoes_complementares.valores_unicos_chave(lista_de_ninhos, condicao)
        if valor_condicao in valores_unicos_condicao:
            lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
            return media_ovos(lista_ninhos_condicao)
        else:
            return -1
    else:
        return -1

def mostra_media_ovos_condicional(lista_de_ninhos):
    condicao = input("Digite a condição (regiao, status, risco, eclosão, predadores): ").lower()
    if condicao in ['regiao', 'status', 'risco', 'predadores']:
        valor_condicao = input(f'Digite o valor para a condição "{condicao}": ').lower()
        if condicao == 'regiao':
            valor_condicao = valor_condicao.title()
        total = media_ovos_condicional(lista_de_ninhos, condicao, valor_condicao)
        if total != -1:
            print(f'Média de ovos para a condição "{condicao}" igual a "{valor_condicao}": {total:.2f}')
        else:
            print("Valor de condição inválido.")
    elif condicao == 'predadores':
        valor_condicao = input('Digite o valor para a condição "predadores" (true/false): ')
        if valor_condicao in ['true', 'false']:
            total = media_ovos_condicional(lista_de_ninhos, 'predadores', valor_condicao)
            if total != -1 and valor_condicao == 'true':
                print('Média de ovos com presença de predadores:', total)
            elif total != -1 and valor_condicao == 'false':
                print('Média de ovos sem presença de predadores:', total)
            else:
                print("Valor de condição inválido.")
        else:
            print("Valor de condição inválido. Use 'true' ou 'false'.")
    elif condicao == 'eclosão':
        valor_condicao = input('Digite o valor para a condição "eclosão" (sim/não): ').lower()
        if valor_condicao in ['sim', 'não']:
            total = media_ovos_condicional(lista_de_ninhos, 'eclosão', valor_condicao)
            if total != -1 and valor_condicao == 'sim':
                print(f'Média de ovos próximos a eclosão: {total:.2f}')
            elif total != -1 and valor_condicao == 'não':
                print(f'Média de ovos não próximos a eclosão: {total:.2f}')
            else:
                print("Valor de condição inválido.")
        else:
            print("Valor de condição inválido. Use 'sim' ou 'não'.")
    else:
        print("Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")
