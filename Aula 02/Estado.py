import os 

class Estado:
    """
    Esta classe recupera informações do estado para o aplicativo de busca
    """
    
    def __init__(self, path=None):
        if path == None:
            #cria o estado inicial
            self.path = self.getEstadoInicial()
        else:
            self.path = path
    
    def getEstadoInicial(self):
        """
        Este método retorna o diretório atual
        """
        estadoInicial= os.path.dirname(os.path.realpath(__file__))
        return estadoInicial
        
    def funcaoSucessora(self):
        """
        Esta é a função sucessora. Gera todo os possiveis
        caminhos que podem ser alcançados a partir do caminho atual.
        """
        if os.path.isdir(self.path):
            lista = [os.path.join(self.path, x) for x in sorted(os.listdir(self.path))]
            return lista
        else:
            return []
            
    def funcaoObjetivo(self):
        """
        Este método verifica se o caminho está no estado objetivo
        """ 
        #verifica de é uma pasta
        if os.path.isdir(self.path):
            return False
        else:
            #separa o nome do arquivo
            fileSeparatorIndex = self.path.rfind(os.sep)
            filename = self.path[fileSeparatorIndex + 1 : ]
            if filename == "f211.txt":
                return True
            else:
                return False  
          