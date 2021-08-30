 
class No:
    """ Esta classe representa um nó na árvore """

    def __init__(self, estado):  # Construtor
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        self.pai = None

    def addFilho(self, no_filho):
        """ Este método adiciona um filho nó ao nó atual """
        
        self.filhos.append(no_filho)
        no_filho.pai = self  # o no_filho aponta para o nó atual
        no_filho.profundidade = self.profundidade + 1
    
    def printArvore(self):
        """ Este método imprime a sub-árvore a partir desse nó """

        print(f"Profundidade: {self.profundidade} - {self.estado.nome}")

        for filho in self.filhos:
            filho.printArvore()

    def printCaminho(self):
        """ Este método imprime o caminho do estado inicial ao estado objetivo """

        if self.pai != None:
            self.pai.printCaminho()  
        
        print("-> ", self.estado.nome)
          