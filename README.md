# Guardião das Tartaruguinhas
## Descrição
Tarefa individual realizada para o curso "Inteligência Artificial Aplicada aos Desafios Socioambientais da Amazônia" do I2A2.

## Cenário
Em uma comunidade ribeirinha da Amazônia, às margens de um igarapé ameaçado por alterações no regime das chuvas e pela presença cada vez maior de embarcações, nasce um esforço coletivo de conservação dos quelônios. Inspirados em projetos regionais como o Pé-de-Pincha, moradores locais, liderados por professores da escola comunitária e jovens voluntários, deram início a um programa de monitoramento artesanal de ninhos de tartarugas. A proposta é garantir que o maior número possível de filhotes chegue com vida ao rio, fortalecendo o ciclo de preservação e a cultura local.

## Anotações dos voluntários
- Região da praia
- Quantidade de ovos
- Estado do ninho
- Risco de alagamento
- Presença de predadores
- Estimativa de dias para eclosão
- Classificação de risco
    - Estável
    - Sob observação
    - Crítico

## Problema
Os dados anotados pelos voluntários são diversos, desorganizados, registrados com variação de escrita, com estrutura inconsistente, sem qualquer forma de agrupamento ou validação.
A falta de estruturação dos dados dificulta a obtenção de respostas sobre o estado dos ninhos e, portanto, o avanço do projeto.

## Objetivo
Criar um sistema local em Python que viabilize a análise e a organização de dados dos ninhos.
Características do sistema:
- Ser simples
- Ser robusto
- Realizar análises por categoria
- Identificar erros ou registros inconsistentes
- Gerar relatórios úteis para a tomada de decisão semanal

Características do código:
- Rodar em Jupyter Notebook
- Interpretável e funcional
- Não utilizar bibliotecas externas
- Usar apenas lógica, estruturas de controle, funções, listas e manipulação direta dos dados
- Ser claro e estruturado em funções

## Tarefas
- [X] Crie uma estrutura de dados usando listas, contendo ao menos 10 ninhos registrados, onde cada ninho será representado como uma sublista ou dicionário contendo os seguintes dados
    - [X] regiao (string): nome da área de praia ("Praia Norte", "Praia Central", etc.)
    - [X] quantidade_ovos (int): número de ovos identificados
    - [X] status (string): "intacto", "ameaçado" ou "danificado“
    - [X] risco (string): "estável", "sob observação" ou "crítico"
    - [X] dias_para_eclosao (int): número estimado de dias restantes
    - [X] predadores (bool): presença de predadores (True ou False)
- [X] Implemente funções para responder às seguintes perguntas
    - [X] Quantos ninhos há no total?
    - [X] Qual a média de ovos por ninho com risco "estável"?
    - [X] Quantos ninhos estão prestes a eclodir (dias ≤ 5)?
    - [X] Qual região tem mais ninhos sob risco?
    - [X] Quantos ninhos têm presença de predadores e estão danificados?
- [X] Crie um menu interativo com input() que permita ao usuário
    - [X] Inserir novos ninhos
    - [X] Visualizar o relatório completo da semana
    - [X] Consultar estatísticas com base nas perguntas acima
    - [X] Encerrar o sistema
- [X] Valide os dados inseridos (ex: não aceitar ovos negativos, status inválido, emojis diferentes dos status, etc.).

Dados iniciais (exemplo mínimo com 5 registros)

ninhos = [
["Praia Norte", 102, "intacto", "estável", 12, False],
["Praia Central", 89, "danificado", "crítico", 3, True],
["Praia Sul", 120, "ameaçado", "sob análise", 7, False],
["Praia Central", 75, "intacto", "estável", 2, False],
["Praia Norte", 60, "danificado", "crítico", 5, True],
]

[!NOTE] Você pode completar até 10 registros ou mais, se desejar.

## Requisitos técnicos
- Você deverá estudar dicionário.
- Usar apenas recursos ensinados até o Encontro 10 acrescido de dicionário.
- Organizar o código em funções reutilizáveis.
- Comentar cada parte para facilitar a leitura.
- O menu deve permitir uso contínuo até o usuário digitar "sair".
- Códigos com soluções criativas ou extras bem estruturadas ganharão destaque.
