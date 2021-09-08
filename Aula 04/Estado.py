
from Mapa import conexoes

class Estado:    
    def __init__(self, lugar=None):
        if lugar is None:
            self.lugar = self.pegaEstadoInicial()  # Cria o estado inicial
        else:
            self.lugar = lugar
    
    def pegaEstadoInicial(self):
        """ Este metodo retorna o estado incial da busca """
        return "Deposito Insumos 1"

    def funcaoSucessora(self):
        """
        Esta é a função sucessora. Gera todo os possiveis
        lugares que podem ser alcançados a partir do estado atual.
        """
        return conexoes[self.lugar]        
        
    def funcaoObjetivo(self):
        """ Este método verifica se o caminho está no estado objetivo (o estado a ser atingido) """
        return self.lugar == "Carregamento"  # Verifica se o lugar atual eh o carregamento
 