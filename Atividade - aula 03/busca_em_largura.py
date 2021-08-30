
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

    print("Fila:")

    while len(fila) > 0:
        no_atual = fila.popleft()                  # Obtem o primeiro item da fila
        print(f"Dequeue: {no_atual.estado.nome}")  # Printa o nó retirado

        if no_atual.estado.funcaoObjetivo():  # Verifica se é o estado meta (o estado a ser buscado)
            print("Atingiu o estado objetivo")
            print("-------------------------")
            print("Caminho (caminho mínimo):")
            no_atual.printCaminho()
            break

        estados_filhos = no_atual.estado.funcaoSucessora()  # Pega os filhos do nó

        for filho in estados_filhos:
            no_filho = No(Estado(filho))

            if no_filho.estado.nome not in visitados:  # Verifica se o nó ainda não foi visitado
                visitados.add(no_filho.estado.nome)    # Coloca na lista de visitados
                no_atual.addFilho(no_filho)            # Adiciona na lista de filhos do nó atual na árvore
                fila.append(no_filho)                  # Coloca na fila


    print("-------------------------\nÁrvore:")
    raiz.printArvore()  # Printa a árvore depois de monta-la (a árvore é montada até atingir o estado objetivo/meta)


if __name__ == "__main__":
    BFS()
      