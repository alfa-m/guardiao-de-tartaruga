## Arquivo funcoes_ninho.py
## Sobre o arquivo:
### Contém as funções relacionadas à criação e validacão de dados dos ninhos

# Importa o módulo com os dados iniciais dos ninhos
import dados_ninho

# Inicializa a lista de ninhos a partir do módulo de dados
lista_de_ninhos = dados_ninho.lista_de_ninhos

## Criação de funções para criação e validação dos dados dos ninhos
# Função que obtém e padronização o valor da chave 'regiao'
def pega_regiao():
    # Solicita ao usuário o nome da região do ninho
    regiao = input("Digite a região do ninho: ")
    ## Verifica se o valor inserido possui apenas letras e espaços
    # Se sim, retorna o valor formatado com a primeira letra de cada palavra maiúscula
    if all(letra.isalpha() or letra.isspace() for letra in regiao):
        return regiao.title()
    # Se não, exibe uma mensagem de erro e solicita a reinserção do valor
    else:
        print("Erro: A região deve conter apenas letras e espaços.")
        return pega_regiao()

# Função que obtém e padronização o valor da chave 'quantidade_ovos'
def pega_quantidade_ovos():
    # Solicita ao usuário a quantidade de ovos
    quantidade_ovos = input("Digite a quantidade de ovos no ninho: ")
    ## Verifica se o valor inserido é um número inteiro positivo
    # Se sim, converte o valor para inteiro e retorna
    if quantidade_ovos.isnumeric() and int(quantidade_ovos) >= 0:
        return int(quantidade_ovos)
    # Se não, exibe uma mensagem de erro e solicita a reinserção do valor
    else:
        print("Erro: A quantidade de ovos deve ser um número inteiro positivo.")
        return pega_quantidade_ovos()

# Funções que obtém e padronização o valor da chave 'status'
def pega_status():
    # Cria uma lista de status válidos
    status_validos = ["intacto", "ameaçado", "danificado"]
    # Solicita ao usuário o status do ninho
    status = input("Digite o status do ninho ('intacto', 'ameaçado' ou 'danificado'): ")
    ## Verifica se o valor inserido está na lista de status válidos
    # Se sim, retorna o valor em minúsculas
    if status.lower() in status_validos:
        return status.lower()
    # Se não, exibe uma mensagem de erro e solicita a reinserção do valor
    else:
        print("Erro: O status deve ser 'intacto', 'ameaçado' ou 'danificado'.")
        return pega_status()

# Função que obtém e padronização o valor da chave 'risco'
def pega_risco():
    # Cria uma lista de riscos válidos
    riscos_validos = ["estável", "sob observação", "crítico"]
    # Solicita ao usuário o risco do ninho
    risco = input("Digite o risco do ninho ('estável', 'sob observação' ou 'crítico'): ")
    ## Verifica se o valor inserido está na lista de riscos válidos
    # Se sim, retorna o valor em minúsculas
    if risco.lower() in riscos_validos:
        return risco.lower()
    # Se não, exibe uma mensagem de erro e solicita a reinserção do valor
    else:
        print("Erro: O risco deve ser 'estável', 'sob observação' ou 'crítico'.")
        return pega_risco()

# Função que obtém e padronização o valor da chave 'dias_para_eclosao'
def pega_dias_para_eclosao():
    # Solicita ao usuário os dias restantes para a eclosão
    dias_para_eclosao = input("Digite os dias restantes para a eclosão: ")
    ## Verifica se o valor inserido é um número inteiro positivo
    # Se sim, converte o valor para inteiro e retorna
    if dias_para_eclosao.isnumeric() and int(dias_para_eclosao) >= 0:
        return int(dias_para_eclosao)
    # Se não, exibe uma mensagem de erro e solicita a reinserção do valor
    else:
        print("Erro: Os dias restantes para a eclosão devem ser um número inteiro positivo.")
        return pega_dias_para_eclosao()

# Função que obtém e padronização o valor da chave 'predadores'  
def pega_predadores():
    # Solicita ao usuário se o ninho tem predadores
    predadores = input("Digite se o ninho tem predadores ('sim' ou 'não'): ")
    ## Verifica se o valor inserido é 'sim' ou 'não'
    # Se o valor for 'sim', retorna True
    if predadores.lower() == "sim":
        return True
    # Se o valor for 'não', retorna False
    elif predadores.lower() == "não":
        return False
    # Se for qualquer outro valor, exibe uma mensagem de erro e solicita a reinserção do valor
    else:
        print("Erro: Resposta inválida. Digite 'sim' ou 'não'.")
        return pega_predadores()

# Função que constrói o dicionário do ninho com as informações coletadas
def constroi_dicionario():
    # Define as chaves válidas para o dicionário do ninho
    chaves_validas = ['regiao', 'quantidade_ovos', 'status', 'risco', 'dias_para_eclosao', 'predadores']

    # Cria um dicionário vazio para o ninho
    ninho = {}

    ## Começa a solicitação de informações do ninho
    # Chama a função de criação da região
    ninho['regiao'] = pega_regiao()
    # Exibe a região
    print("Região do ninho:", ninho['regiao'])

    # Chama a função de criação de quantidade de ovos
    ninho['quantidade_ovos'] = pega_quantidade_ovos()
    # Exibe a quantidade de ovos
    print("Quantidade de ovos no ninho:", ninho['quantidade_ovos'])

    # Chama a função de criação de status
    ninho['status'] = pega_status()
    # Exibe o status
    print("Status do ninho:", ninho['status'])

    # Chama a função de criação de risco
    ninho['risco'] = pega_risco()
    # Exibe o risco
    print("Risco do ninho:", ninho['risco'])

    # Chama a função de criação de dias para a eclosão
    ninho['dias_para_eclosao'] = pega_dias_para_eclosao()
    # Exibe os dias para a eclosão
    print("Dias restantes para a eclosão:", ninho['dias_para_eclosao'])

    # Chama a função de criação de predadores
    ninho['predadores'] = pega_predadores()
    # Exibe os predadores
    print("Ninho tem predadores:", ninho['predadores'])

    ## Verifica se as chaves utilizadas são chaves válidas
    # Se não forem, exibe uma mensagem de erro e reinicializa o processo
    if not all(key in ninho for key in chaves_validas):
        print("Erro: Informações incompletas. O ninho não será adicionado.")
        return constroi_dicionario()
    # Se forem, verifica se há valores vazios
    else:
        # Se houver algum valor vazio, exibe uma mensagem de erro e encerra a função
        if any(ninho.get(key) is None for key in chaves_validas):
            print("Erro: Informações incompletas. O ninho não será adicionado.")
            return None
        # Senão, adiciona o ninho à lista de ninhos e exibe uma mensagem de sucesso
        else:
            lista_de_ninhos.append(ninho)
            print("Dicionário de ninho construído com sucesso!")
            return ninho

# Função que exibe os ninhos salvos na lista de ninhos
def exibe_ninhos():
    ## Verifica se a lista de ninhos está vazia
    # Se estiver, informa que a lista está vazia
    if not lista_de_ninhos:
        print("Nenhum ninho registrado.")
    # Senão, mostra cada ninho
    else:
        print("Lista de ninhos registrados:")
        # Para cada ninho, é mostrada sua posição na lista de ninhos
        for i, ninho in enumerate(lista_de_ninhos, start=1):
            print(f"Ninho {i}:")
            # É mostrado cada par de chave e valor do dicionário do ninho atual
            for chave, valor in ninho.items():
                print(f"  {chave}: {valor}")
            print()
