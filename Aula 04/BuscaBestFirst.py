
from Estado import Estado
from No import No
import queue
    
def executaBuscaBestFirst():
    """ Esse metodo implementa a Busca Best First """    
    
    fila_prioridade = queue.PriorityQueue()  # Cria a fila de prioridade
    visitado = []  # Lista com nos visitados
    
    # Cria o no raiz
    estadoInicial = Estado()  
    raiz = No(estadoInicial, None)  # O nó pai do nó raiz é None
    
    # Adiciona na fila de prioridade e na lista de visitados
    fila_prioridade.put((raiz.heuristica, raiz))
    visitado.append(raiz.estado.lugar)
 
    # Verifica se há um nó na fila de prioridade
    while not fila_prioridade.empty(): 
        # Retira o primeiro nó da fila de prioridade (o retorno é (priority_number, data) -> (função heuristica, nó atual))
        # _ é váriavel oculta
        _, no_atual = fila_prioridade.get()

        no_atual.fringe = False  # Remove da fringe
        
        print("-- Nó Atual --", no_atual.estado.lugar)
        
        if no_atual.estado.funcaoObjetivo():  # Verifica se esse eh o estado meta
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
                
    print("-" * 58)
    print("Arvore:")
    raiz.printArvore()


if __name__ == "__main__":
    executaBuscaBestFirst()
      