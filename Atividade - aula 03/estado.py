
import grafo

class Estado:
    def __init__(self, nome=None):
        if nome == None:
            self.nome = self.getEstadoInicial()  # Cria o estado inicial
        else:
            self.nome = nome

    def getEstadoInicial(self):
        """ Este método retorna o nome Casa (o estado inicial) """
        return "Casa"
    
    def funcaoSucessora(self):
        """ Esta é a função sucessora. Ela encontra todas os locais conectados com o local atual """
        return grafo.conexoes[self.nome]

    def funcaoObjetivo(self):
        """ Esse método verifica se o local foi atingido, ou seja, se é Faculdade Impacta """ 
        return self.nome == "Faculdade Impacta"
          