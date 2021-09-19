
from mapa import conexoes

class Estado:    
    def __init__(self, posicao=None, destino=None):
        if posicao is None:
            self.posicao = self.pegaEstadoInicial()  # Cria o estado inicial
        else:
            self.posicao = posicao

        if destino is None:
            self.destino = "Carregamento"  # Estado meta padrão
        else:
            self.destino = destino
    
    def pegaEstadoInicial(self):
        """ Este metodo retorna o estado incial da busca """
        return "Deposito Insumos 1"

    def funcaoSucessora(self):
        """ Gera todo os possiveis lugares que podem ser alcançados a partir do estado atual. """
        return conexoes[self.posicao]        
        
    def funcaoObjetivo(self):
        """ Este método verifica se o caminho está no estado objetivo (o estado a ser atingido) """
        return self.posicao == self.destino
   