
import mapa
import math

class No:
    """ Essa classe representa um nó na arvore de busca. """

    def __init__(self, estado, no_pai):
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        
        if no_pai is not None:
            no_pai.filhos.append(self)
            self.pai = no_pai
            self.profundidade = no_pai.profundidade + 1
        else:
            self.pai = None

        self.fringe = True  # Se o nó faz parte do fringe (borda, os nós inexplorados, que estão na fila de prioridade)
        self.heuristica = 0
        self.calculaHeuristica()
    
    def addFilho(self, no_filho):
        """ Este método adiciona um nó em outro nó """

        self.filhos.append(no_filho)
        no_filho.pai = self   # o no_filho aponta para o nó atual
        no_filho.profundidade = self.profundidade + 1

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
        estado meta (estado a ser atingido/objetivo), que é o cálculo da distancia entre dois pontos no plano cartesiano.
        Distancia = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
        """
        
        localizacao_meta = mapa.localizacao["Faculdade Impacta"]  # Localizacao destino
        localizacao_atual = mapa.localizacao[self.estado.lugar]   # Localização atual
        dx = localizacao_meta[0] - localizacao_atual[0]           # Delta na coordenada x
        dy = localizacao_meta[1] - localizacao_atual[1]           # Delta na coordenada y
        distancia = math.sqrt(dx ** 2 + dy ** 2)                  # Distancia
        self.heuristica = distancia

        print(f"Função heurística para '{self.estado.lugar}': {distancia}")
          