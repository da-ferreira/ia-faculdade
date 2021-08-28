
from GrafoDados import conexoes

class Estado:
    """ Esta classe recupera informações de estado de um aplicatico de conexão social """
    
    def __init__(self, nome=None):
        if nome == None:
            self.nome = self.getEstadoInicial()  # Cria o estado inicial
        else:
            self.nome = nome
            
    def getEstadoInicial(self):
        """ Este método retorna o nome Ana """
        estadoInicial = "Ana"
        return estadoInicial

    def funcaoSucessora(self):
        """ Esta é a função sucessora. Ela encontra todas as pessoas conectados com a pessoa atual """
        return conexoes[self.nome]
        
    def funcaoObjetivo(self):
        """ Esse método verifica se a pessoa é Gil """ 
        return self.nome == "Gil"
          