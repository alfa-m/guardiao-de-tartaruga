## Arquivo dados_ninho.py
## Sobre o arquivo:
### Contém os dados iniciais dos ninhos de tartarugas marinhas

## Sobre os dados:
### Cada ninho é representado por um dicionário com as informações solicitadas
### Chaves do dicionário:
### - 'regiao' -> Recebe valor do tipo string, representando a região onde o ninho está localizado
### - 'quantidade_ovos' -> Recebe valor do tipo inteiro, representando a quantidade de ovos no ninho
### 'status' -> Recebe valor do tipo string, representando o status do ninho
### 'risco' -> Recebe valor do tipo string, representando o risco do ninho
### 'dias_para_eclosao' -> Recebe valor do tipo inteiro, representando a quantidade de dias restantes para a eclosão dos ovos
### 'predadores' -> Recebe valor do tipo booleano, indicando se há predadores na região do ninho

# Criação dos ninhos iniciais
ninho_1 = {'regiao': 'Praia Norte', 'quantidade_ovos': 102, 'status': 'intacto',
      'risco': 'estável', 'dias_para_eclosao': 12, 'predadores': False}
ninho_2 = {'regiao': 'Praia Central', 'quantidade_ovos': 89, 'status': 'danificado',
      'risco': 'crítico', 'dias_para_eclosao': 3, 'predadores': True}
ninho_3 = {'regiao': 'Praia Sul', 'quantidade_ovos': 120, 'status': 'ameaçado',
      'risco': 'sob observação', 'dias_para_eclosao': 7, 'predadores': False}
ninho_4 = {'regiao': 'Praia Central', 'quantidade_ovos': 75, 'status': 'intacto',
      'risco': 'estável', 'dias_para_eclosao': 2, 'predadores': False}
ninho_5 = {'regiao': 'Praia Norte', 'quantidade_ovos': 60, 'status': 'danificado',
      'risco': 'crítico', 'dias_para_eclosao': 5, 'predadores': True}
ninho_6 = {'regiao': 'Praia Sudeste', 'quantidade_ovos': 110, 'status': 'intacto',
      'risco': 'estável', 'dias_para_eclosao': 10, 'predadores': False}
ninho_7 = {'regiao': 'Praia Nordeste', 'quantidade_ovos': 95, 'status': 'ameaçado',
      'risco': 'sob observação', 'dias_para_eclosao': 8, 'predadores': True}
ninho_8 = {'regiao': 'Praia Sudoeste', 'quantidade_ovos': 80, 'status': 'intacto',
      'risco': 'estável', 'dias_para_eclosao': 4, 'predadores': False}
ninho_9 = {'regiao': 'Praia Noroeste', 'quantidade_ovos': 70, 'status': 'danificado',
      'risco': 'crítico', 'dias_para_eclosao': 1, 'predadores': True}
ninho_10 = {'regiao': 'Praia Leste', 'quantidade_ovos': 85, 'status': 'intacto',
      'risco': 'estável', 'dias_para_eclosao': 6, 'predadores': False}
ninho_11 = {'regiao': 'Praia Oeste', 'quantidade_ovos': 50, 'status': 'ameaçado',
      'risco': 'sob observação', 'dias_para_eclosao': 9, 'predadores': True}

# Criação da lista de ninhos
lista_de_ninhos = [ninho_1, ninho_2, ninho_3, ninho_4, ninho_5,
                   ninho_6, ninho_7, ninho_8, ninho_9, ninho_10,
                   ninho_11]
