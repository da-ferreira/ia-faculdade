
import mapa

class Estado:
    def __init__(self, lugar=None):
        if lugar is None:
            self.lugar = self.pegaEstadoInicial()  # Cria o estado inicial
        else:
            self.lugar = lugar

    def pegaEstadoInicial(self):
        """ Este metodo retorna o estado incial da busca """
        return "Casa"

    def funcaoSucessora(self):
        """
        Gera todo os possiveis lugares que podem ser alcançados a partir do estado atual.
        """
        return mapa.conexoes[self.lugar]        
        
    def funcaoObjetivo(self):
        """ Este metodo verifica se o caminho está no estado objetivo (o estado a ser atingido) """
        return self.lugar == "Faculdade Impacta"
  