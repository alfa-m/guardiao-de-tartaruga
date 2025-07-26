import funcoes_complementares

def total_ninhos(lista_de_ninhos):
    return len(lista_de_ninhos)

def mostra_total_ninhos(lista_de_ninhos):
    total = total_ninhos(lista_de_ninhos)
    if total != 0:
        print('Total de ninhos registrados:', total)
    else:
        print("Não há nenhum ninho registrado.")

def lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao):
    if condicao == 'eclosão' and valor_condicao == 'sim':
        return [ninho for ninho in lista_de_ninhos if ninho['dias_para_eclosao'] <= 5]
    elif condicao == 'eclosão' and valor_condicao == 'não':
        return [ninho for ninho in lista_de_ninhos if ninho['dias_para_eclosao'] > 5]
    else:
        return [ninho for ninho in lista_de_ninhos if ninho[condicao] == valor_condicao]

def total_ninhos_condicional(lista_de_ninhos, condicao, valor_condicao):
    if condicao == 'eclosão':
        lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
        return total_ninhos(lista_ninhos_condicao)
    elif condicao in ['regiao', 'status', 'risco', 'predadores']:
        valores_unicos_condicao = funcoes_complementares.valores_unicos_chave(lista_de_ninhos, condicao)
        if valor_condicao in valores_unicos_condicao:
            lista_ninhos_condicao = lista_ninhos_condional(lista_de_ninhos, condicao, valor_condicao)
            return total_ninhos(lista_ninhos_condicao)
        else:
            return -1

def mostra_total_ninhos_condicional(lista_de_ninhos):
    condicao = input("Digite a condição (regiao, status, risco, eclosão, predadores): ").lower()
    if condicao in ['regiao', 'status', 'risco', 'predadores']:
        valor_condicao = input(f'Digite o valor para a condição "{condicao}": ').lower()
        if condicao == 'regiao':
            valor_condicao = valor_condicao.title()
        total = total_ninhos_condicional(lista_de_ninhos, condicao, valor_condicao)
        if total != -1:
            print(f'Total de ninhos para a condição "{condicao}" igual a "{valor_condicao}":', total)
        else:
            print("Valor de condição inválido.")
    elif condicao == 'eclosão':
        valor_condicao = input('Digite o valor para a condição "eclosão" (sim/não): ').lower()
        if valor_condicao in ['sim', 'não']:
            total = total_ninhos_condicional(lista_de_ninhos, 'eclosão', valor_condicao)
            if total != -1 and valor_condicao == 'sim':
                print(f'Total de ninhos próximos a eclosão:', total)
            elif total != -1 and valor_condicao == 'não':
                print(f'Total de ninhos não próximos a eclosão:', total)
            else:
                print("Valor de condição inválido.")
        else:
            print("Valor de condição inválido. Use 'sim' ou 'não'.")
    else:
        print("Condição inválida. Use 'regiao', 'status', 'risco' ou 'predadores'.")

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
