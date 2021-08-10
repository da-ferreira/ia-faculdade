class No:
    '''
    Esta classe representa um nó na árvore de busca
    '''
    
    def __init__(self, estado):
        """
        Construtor
        """
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        self.pai = None
        
        
    def addFilho(self, noFilho):
        """
        Este método adiciona um nó em outro nó
        """
        self.filhos.append(noFilho)
        noFilho.pai = self  # O nó filho aponta para o nó atual (o pai dele)
        noFilho.profundidade = self.profundidade + 1
        
    
    def printArvore(self):
        """
        Este método imprime a árvore
        """
        print (self.profundidade , " - " , self.estado.path)
        for child in self.filhos:
            child.printArvore()
            
            