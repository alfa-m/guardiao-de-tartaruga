lista_de_ninhos = []

def pega_regiao():
    regiao = input("Digite a região do ninho: ")
    if all(letra.isalpha() or letra.isspace() for letra in regiao):
        return regiao.title()
    else:
        print("Erro: A região deve conter apenas letras e espaços.")
        return pega_regiao()

def pega_quantidade_ovos():
    quantidade_ovos = input("Digite a quantidade de ovos no ninho: ")
    if quantidade_ovos.isnumeric() and int(quantidade_ovos) >= 0:
        return int(quantidade_ovos)
    else:
        print("Erro: A quantidade de ovos deve ser um número inteiro positivo.")
        return pega_quantidade_ovos()

def pega_status():
    status = input("Digite o status do ninho ('intacto', 'ameaçado' ou 'danificado'): ")
    status_validos = ["intacto", "ameaçado", "danificado"]
    if status.lower() in status_validos:
        return status.lower()
    else:
        print("Erro: O status deve ser 'intacto', 'ameaçado' ou 'danificado'.")
        return pega_status()

def pega_risco():
    risco = input("Digite o risco do ninho ('estável', 'sob observação' ou 'crítico'): ")
    riscos_validos = ["estável", "sob observação", "crítico"]
    if risco.lower() in riscos_validos:
        return risco.lower()
    else:
        print("Erro: O risco deve ser 'estável', 'sob observação' ou 'crítico'.")
        return pega_risco()

def pega_dias_para_eclosao():
    dias_para_eclosao = input("Digite os dias restantes para a eclosão: ")
    if dias_para_eclosao.isnumeric() and int(dias_para_eclosao) >= 0:
        return int(dias_para_eclosao)
    else:
        print("Erro: Os dias restantes para a eclosão devem ser um número inteiro positivo.")
        return pega_dias_para_eclosao()
    
def pega_predadores():
    predadores = input("Digite se o ninho tem predadores ('sim' ou 'não'): ")
    if predadores.lower() == "sim":
        return predadores == True
    elif predadores.lower() == "não":
        return predadores == False
    else:
        print("Erro: Resposta inválida. Digite 'sim' ou 'não'.")
        return pega_predadores()

def constroi_dicionario():
    chaves_validas = ['regiao', 'quantidade_ovos', 'status', 'risco', 'dias_para_eclosao', 'predadores']

    print("Construindo dicionário de ninhos...")
    ninho = {}
    ninho['regiao'] = pega_regiao()
    print("Região do ninho:", ninho['regiao'])

    ninho['quantidade_ovos'] = pega_quantidade_ovos()
    print("Quantidade de ovos no ninho:", ninho['quantidade_ovos'])

    ninho['status'] = pega_status()
    print("Status do ninho:", ninho['status'])

    ninho['risco'] = pega_risco()
    print("Risco do ninho:", ninho['risco'])

    ninho['dias_para_eclosao'] = pega_dias_para_eclosao()
    print("Dias restantes para a eclosão:", ninho['dias_para_eclosao'])

    ninho['predadores'] = pega_predadores()
    print("Ninho tem predadores:", ninho['predadores'])

    if not all(key in ninho for key in chaves_validas):
        print("Erro: Informações incompletas. O ninho não será adicionado.")
        return constroi_dicionario()
    else:
        lista_de_ninhos.append(ninho)
        print("Dicionário de ninho construído com sucesso!")
        return ninho

def exibe_ninhos():
    if not lista_de_ninhos:
        print("Nenhum ninho registrado.")
    else:
        print("Lista de ninhos registrados:")
        for i, ninho in enumerate(lista_de_ninhos, start=1):
            print(f"Ninho {i}:")
            for chave, valor in ninho.items():
                print(f"  {chave}: {valor}")
            print()
