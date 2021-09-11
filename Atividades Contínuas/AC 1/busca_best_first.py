
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
        _, no_atual = fila_prioridade.get()
        no_atual.fringe = False  # Remove o nó da fringe

        print(f"Nó atual: {no_atual.estado.lugar}")

        if no_atual.estado.funcaoObjetivo():  # Verifica se esse é o estado meta
            print("Estado meta alcançado!")
            print("-" * 58)
            print("Caminho:")
            no_atual.printCaminho()
            break

        estados_filhos = no_atual.estado.funcaoSucessora()  # Pega os nós filhos

        for filho in estados_filhos:
            if filho not in visitados:
                no_filho = No(Estado(filho), no_atual)                # Cria um nó e coloca na arvore
                fila_prioridade.put((no_filho.heuristica, no_filho))  # Coloca o nó criado na fila de prioridade
                visitados.add(filho)                                  # Coloca o estado filho na lista de visitados
    
    print("-" * 58)
    print("Árvore:")
    raiz.printArvore()


if __name__ == "__main__":
    busca_best_first()
 