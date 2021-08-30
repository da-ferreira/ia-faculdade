
from no import No
from estado import Estado
from collections import deque

def BFS():
    """ Esta função executa a pesquisa BFS (busca em largura) usando uma fila """

    fila = deque([])
    visitados = set()    # Lista de visitados para controlar a visita nos vértices do grafo
    raiz = No(Estado())  # Cria o nó raiz da árvore

    # Adiciona à fila e a lista de visitados
    fila.append(raiz)
    visitados.add(raiz.estado.nome)

    while len(fila) > 0:
        pass