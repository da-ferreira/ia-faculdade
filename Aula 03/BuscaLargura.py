
from No import No
from Estado import Estado
from collections import deque

def executaBFS():
    """
    Esta função executa a pesquisa BFS usando uma fila
    """
    #criar fila
    fila = deque([])
    
    #por ser um gráfico, criamos uma lista de visitantes
    visitados = []
    
    #criar nó raiz
    estadoInicial = Estado()
    raiz = No(estadoInicial)
    #adicionar à fila e lista de visitados
    fila .append(raiz)    
    visitados.append(raiz.estado.nome)
    
    # verifique se há algo na para retirar da fila (dar o  dequeue)
    while len(fila) > 0:
        
        #obtem o primeiro item da fila
        noAtual = fila.popleft()
        
        print ("-- dequeue --", noAtual.estado.nome)
        
        #verifica se é o estado meta
        if noAtual.estado.funcaoObjetivo():
            print ("Atingiu o estado objetivo")
            #faz o print do caminho
            print ("----------------------")
            print ("Caminho")
            noAtual.printCaminho()
            break
            
        #pega os nos filhos
        estadosFilhos = noAtual.estado.funcaoSucessora()
        for estadoFilho in estadosFilhos:
            
            noFilho = No(Estado(estadoFilho))
            
            #verifica se o no ainda não foi visitado
            if noFilho.estado.nome not in visitados:
                
                #coloca na lista de nos visitados
                visitados.append(noFilho.estado.nome )
                
                #coloca na arvore e na fila
                noAtual.addFilho(noFilho)
                fila.append(noFilho)       
            
    #print arvore
    print ("----------------------")
    print ("Arvore")
    raiz.printArvore()  
  