
from Estado import Estado
from No import No

class BuscaEmProfundidade():
    """
    Essa classe executa uma Busca em Profundidade Recursiva
    """
    def __init__(self):
        self.achou = False
        
    def busca(self):
        """
        Este método inicia a busca
        """
        #pega o estado inicial
        estadoInicial = Estado('C:/Users/Home/Desktop/CC - 4°/Inteligência Artificial/IA Algoritmos/Aula 02/DiretorioInicial')
        
        #cria o nó raiz
        noRaiz = No(estadoInicial)
        
        #realizar a busca a partir do nó raiz
        self.DFS(noRaiz)
        
        noRaiz.printArvore()
        
    def DFS(self, no):
        """
        Isso cria a árvore de busca
        """
        if not self.achou:
            print ("-- proc --", no.estado.caminho)
            
            # verifica se foi atingido o estado meta
            if no.estado.funcaoObjetivo():
                print ("Atingido o estado de meta")
                self.achou = True
                
            else:
                # encontra os estados sucessores do estado atual
                estadosFilhos = no.estado.funcaoSucessora()
                
                # adiciona os nós filhos na árvore
                for estadoFilho in estadosFilhos:
                    noFilho = No(Estado(estadoFilho))
                    no.addFilho(noFilho) 
                    # faz a busca em um dos nós filhos
                    self.DFS(noFilho)
          