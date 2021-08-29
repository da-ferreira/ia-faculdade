
""" Cria o dicionário com as conexões do grafo """

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
 
if __name__ == "__main__":
    for vertice in conexoes:
        print(f'{vertice}: {conexoes[vertice]}')