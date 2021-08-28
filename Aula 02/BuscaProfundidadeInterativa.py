
from No import No
from Estado import Estado

""" Solução interativa para a busca em profundidade. Nessa solução uma estrutura de pilha é utilizada. """

def buscaEmProfundidadeInterativa():
    """
    Esta função realiza busca em profundidade usando uma pilha
    """
    #cria pilha
    pilha = []
    
    #cria o no raiz e o coloca na pilha
    estadoInicial = Estado('C:/Users/Home/Desktop/CC - 4°/Inteligência Artificial/IA Algoritmos/Aula 02/DiretorioInicial')
    raiz = No(estadoInicial)
    pilha.append(raiz)
    
    #verifica se há algo na pilha para dar um pop
    while len(pilha) > 0:
        
        #pop no nó do topo
        nohCorrente = pilha.pop()
        
        print ("-- pop --", nohCorrente.estado.caminho)
        
        #verifique se este é o estado da meta
        if nohCorrente.estado.funcaoObjetivo():
            print ("Chegou ao estado meta!")
            break
            
        #obtem os nós filhos
        estadosFilhos= nohCorrente.estado.funcaoSucessora() 
        for estFilho in estadosFilhos:
            nohFilho = No(Estado(estFilho))
            nohCorrente.addFilho(nohFilho)
        
        #em ordem reversa adicionar nó à pilha
        for index in range(len(nohCorrente.filhos) - 1, -1, -1):
            pilha.append(nohCorrente.filhos[index])
    
    
    #mostra a árvore
    print ("----------------------")
    raiz.printArvore()
    
    
if __name__ == "__main__":
    buscaEmProfundidadeInterativa()
