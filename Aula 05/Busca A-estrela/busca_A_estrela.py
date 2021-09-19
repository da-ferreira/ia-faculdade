
from estado import Estado
from no import No
from queue import PriorityQueue

def busca_A_estrela():
    """ Implementa a Busca A* """    
    
    fila_prioridade = PriorityQueue()  # Cria a fila de prioridade
    visitado = []  # Lista com nos visitados
    raiz = No(Estado(), None)  # Cria o no raiz. O nó pai do nó raiz é None

    # Adiciona na fila de prioridade e na lista de visitados
    fila_prioridade.put((raiz.heuristica, raiz))
    visitado.append(raiz.estado.posicao)

    while not fila_prioridade.empty(): 
        _, no_atual = fila_prioridade.get()

        no_atual.fringe = False  # Remove da fringe
        print(f"-- Nó atual -- {no_atual.estado.posicao}")

        if no_atual.estado.funcaoObjetivo():  # Verifica se esse é o estado meta
            print("Alcancado o estado meta")
            print("-" * 58)
            print("Caminho:")
            no_atual.printCaminho()
            break

        estados_fihos = no_atual.estado.funcaoSucessora()  # Pega os nós filhos

        for estado_filho in estados_fihos :
            if estado_filho not in visitado:                          # Verifica se o nó ainda nao foi visitado
                no_filho = No(Estado(estado_filho), no_atual)         # Cria um nó e coloca na arvore
                fila_prioridade.put((no_filho.heuristica, no_filho))  # Coloca na fila de prioridade
                visitado.append(no_filho.estado.posicao)              # Coloca o nó na lista de visitados
    
    print("-" * 58)
    print("Arvore:")
    raiz.printArvore()


if __name__ == "__main__":
    busca_A_estrela()
  