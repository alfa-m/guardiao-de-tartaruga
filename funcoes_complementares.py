def valores_unicos_chave(lista_dicionarios, chave):
    valores_unicos = set()
    for dicionario in lista_dicionarios:
        if chave in dicionario:
            valores_unicos.add(dicionario[chave])
    return valores_unicos
