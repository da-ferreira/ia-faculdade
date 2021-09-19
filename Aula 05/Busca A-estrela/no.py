
from mapa import localizacao
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
        self.calculaCusto()
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

        print(f"Profundidade: {self.profundidade} - {self.estado.posicao}")
        
        for filho in self.filhos:
            filho.printArvore()
                       
    def printCaminho(self):
        """ Este metdo faz um print do estado inicial ate o estado meta (estado objetico) """
        
        if self.pai != None:
            self.pai.printCaminho()

        print ("-> ", self.estado.posicao)
    
    def calculaDistancia(self, local1, local2):
        """ Calcula a distancia entre dois pontos """
        
        dx = local1[0] - local2[0]  # Delta na coordenada x
        dy = local1[1] - local2[1]  # Delta na coordenada y
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        return distancia

    def calculaCusto(self):
        """ Calcula a distancia do nó atual ate o no raiz """
        
        if self.pai != None:
            # Encontra distância do nó atual ao pai
            distancia = self.calculaDistancia(localizacao[self.estado.posicao], localizacao[self.pai.estado.posicao])
            # custo = custo do pai + distancia
            self.custo_ate_raiz = self.pai.custo_ate_raiz + distancia 
        else:
            self.custo_ate_raiz = 0
        
    def calculaHeuristica(self):
        """ Calcula o valor heuristico do nó """        

        # Encontra a distância entre este estado e o estado objetivo
        local_meta = localizacao[self.estado.destino]  
        local_corrente = localizacao[self.estado.posicao]
        distancia_para_meta = self.calculaDistancia(local_meta, local_corrente)
        
        heuristica = self.custo_ate_raiz + distancia_para_meta  # Usa a distancia para formar um valor heurístico
        self.heuristica = heuristica

        print(f"Heurística para {self.estado.posicao}: {heuristica} ({self.custo_ate_raiz}, {distancia_para_meta})")
           