
""" Cria o dicionário com as conexões do grafo e a localização (coordenadas x e y) do mapa topológico """

conexoes = {
    'Casa':              {'Ponto de Onibus 1', 'Uber'},
    'Ponto de Onibus 1': {'Casa', 'CPTM L9', 'Ponto de Onibus 2', 'Metro L5'},
    'CPTM L9':           {'Ponto de Onibus 1', 'CPTM L8'},
    'Uber':              {'Casa', 'Faculdade Impacta'},
    'Metro L5':          {'Ponto de Onibus 1', 'Metro L1'},
    'Ponto de Onibus 2': {'Ponto de Onibus 1', 'Ponto de Onibus 3'},
    'CPTM L8':           {'CPTM L9', 'Faculdade Impacta'},
    'Metro L1':          {'Metro L5', 'Ponto de Onibus 3', 'Taxi'},
    'Ponto de Onibus 3': {'Ponto de Onibus 2', 'Metro L1', 'Faculdade Impacta'},
    'Taxi':              {'Metro L1', 'Faculdade Impacta'},
    'Faculdade Impacta': {'Taxi', 'Ponto de Onibus 3', 'CPTM L8', 'Uber'}
}
 
localizacao = {
    'Casa': [1, 9],
    'Ponto de Onibus 1': [4, 12],
    'CPTM L9': [5, 8],
    'Uber': [5, 0],
    'Metro L5': [8, 14],
    'Ponto de Onibus 2': [6, 10],
    'CPTM L8': [7, 4],
    'Metro L1': [11, 12],
    'Ponto de Onibus 3': [9, 7],
    'Taxi': [12, 9],
    'Faculdade Impacta': [15, 6]
}
