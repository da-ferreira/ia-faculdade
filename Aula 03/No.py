
class No:
    """ Esta classe representa um nó na árvore de busca """
    
    def __init__(self, estado):
        """ Construtor """

        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        self.pai = None
        
    def addFilho(self, noFilho):
        """ Este método adiciona um nó em outro nó """

        self.filhos.append(noFilho)
        noFilho.pai = self   # o noFilho aponta para o nó atual
        noFilho.profundidade = self.profundidade + 1
    
    def printArvore(self):
        """ Este método imprime a sub-árvore a partir desse nó """

        print(self.profundidade, " - " , self.estado.nome)
        
        for umFilho in self.filhos:
            umFilho.printArvore()
            
    def printCaminho(self):
        """ Este método imprime o caminho do estado inicial ao estado objetivo """

        if self.pai != None:
            self.pai.printCaminho()  
        
        print("-> ", self.estado.nome)
           