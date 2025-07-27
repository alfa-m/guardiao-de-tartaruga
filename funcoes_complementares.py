## Arquivo funcoes_complementares.py
## Sobre o arquivo:
### Contém as funções auxiliares

# Função que retorna os valores únicos para uma determinada chave de  dicionário
def valores_unicos_chave(lista_dicionarios, chave):
    # Cria uma lista para armazenar os valores únicos
    valores_unicos = set()
    # Para cada dicionário na lista de dicionários, verifica se a desejada chave está contida no dicionário
    for dicionario in lista_dicionarios:
        # Se a chave está no dicionário, adiciona o valor único na lista de valores únicos
        if chave in dicionario:
            valores_unicos.add(dicionario[chave])
    return valores_unicos
