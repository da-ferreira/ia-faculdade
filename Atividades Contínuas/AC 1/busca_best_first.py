
from estado import Estado
from no import No
from queue import PriorityQueue

def busca_best_first():
    """ Implementação da busca Best First """

    fila_prioridade = PriorityQueue()  # Cria a fila de prioridade
    visitados = set()                  # Lista com os nós visitados
    raiz = No(Estado(), None)          # Cria o nó raiz. O pai do raíz é nulo
    
    # Adiciona raiz na fila de prioridade e na lista de visitados
    fila_prioridade.put((raiz.heuristica, raiz))
    visitados.add(raiz.estado.lugar)

    while not fila_prioridade.empty():
        break

if __name__ == "__main__":
    busca_best_first()
