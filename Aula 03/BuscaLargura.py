
from No import No
from Estado import Estado
from collections import deque

def executaBFS():
    """ Esta função executa a pesquisa BFS usando uma fila """
    
    fila = deque([])
    visitados = []   # Por ser um gráfico, criamos uma lista de visitantes
    
    # Cria nó raiz
    estadoInicial = Estado()  
    raiz = No(estadoInicial)
    
    # Adiciona à fila e a lista de visitados
    fila.append(raiz)    
    visitados.append(raiz.estado.nome)
        
    while len(fila) > 0:          # Verifica se há algo para retirar da fila (dar o  dequeue)        
        noAtual = fila.popleft()  # Obtem o primeiro item da fila
        
        print ("-- dequeue --", noAtual.estado.nome)
        
        if noAtual.estado.funcaoObjetivo():  # Verifica se é o estado meta (o estado a ser buscado)
            print ("Atingiu o estado objetivo")
            
            # Faz o print do caminho
            print ("----------------------")
            print ("Caminho:")
            noAtual.printCaminho()
            break
            
        estadosFilhos = noAtual.estado.funcaoSucessora()  # Pega os nos filhos
        
        for estadoFilho in estadosFilhos:    
            noFilho = No(Estado(estadoFilho))
                        
            if noFilho.estado.nome not in visitados:   # Verifica se o nó ainda não foi visitado
                visitados.append(noFilho.estado.nome)  # Coloca na lista de nos visitados
                
                # Coloca na arvore e na fila
                noAtual.addFilho(noFilho)
                fila.append(noFilho)       
            
    # Printa a árvore
    print ("----------------------")
    print ("Arvore:")
    raiz.printArvore()  
  