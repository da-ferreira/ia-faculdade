
from Mapa import localizacao
import math

class No:
    """ Essa classe representa um noh na arvore de busca. """
    
    def __init__(self, estado, no_pai):  # Construtor
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        self.colocaPai(no_pai)  # self.pai = None
        self.fringe = True     # Se o nó faz parte do fringe (borda, os nós inexplorados, que estão na fila de prioridade)
        self.heuristica = 0
        self.calculaHeuristica()
               
    def colocaPai(self, no_pai):
        """ Esse metodo adiciona um nó em outro nó """

        if no_pai is not None:
            no_pai.filhos.append(self)
            self.pai = no_pai
            self.profundidade = no_pai.profundidade + 1
        else:
            self.pai = None

    def addFilho(self, noFilho):
        """ Este método adiciona um nó em outro nó """

        self.filhos.append(noFilho)
        noFilho.pai = self   # o noFilho aponta para o nó atual
        noFilho.profundidade = self.profundidade + 1
           
    def printArvore(self):
        """ Este metodo faz um print da arvore de busca, a partir do nó chamado. """

        print(f"Profundidade: {self.profundidade} - {self.estado.lugar}")
        
        for filho in self.filhos:
            filho.printArvore()
                       
    def printCaminho(self):
        """ Este metdo faz um print do estado inicial ate o estado meta (estado objetico) """
        
        if self.pai != None:
            self.pai.printCaminho()

        print ("-> ", self.estado.lugar)
        
    def calculaHeuristica(self):
        """ 
        Essa funcao calcula o valor da função heuristica para esse nó, calculando a distancia do estado atual para o
        estado meta (estado a ser atingido/objetivo), que é o calculo da distancia entre dois pontos no plano cartesiano.
        Distancia = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
        """
        
        localizacaoMeta = localizacao["Carregamento"]      # Localizacao destino
        localizacaoAtual = localizacao[self.estado.lugar]  # Localização atual
        dx = localizacaoMeta[0] - localizacaoAtual[0]      # Delta na coordenada x
        dy = localizacaoMeta[1] - localizacaoAtual[1]      # Delta na coordenada y
        distancia = math.sqrt(dx ** 2 + dy ** 2)           # Distancia
        self.heuristica = distancia

        print(f"Função heurística para {self.estado.lugar}: {distancia}")
         