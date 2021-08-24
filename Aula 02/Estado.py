
import os 

class Estado:
    '''
    Esta classe recupera informações do estado para o aplicativo de busca
    '''
    
    # Construtor
    def __init__(self, caminho = None):  
        if caminho == None:
            #cria o estado inicial
            self.caminho = self.getEstadoInicial()
        else:
            self.caminho = caminho
    
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
        if os.path.isdir(self.caminho): #verifica se eh um diretório
            lista = [os.path.join(self.caminho, x) for x in sorted(os.listdir(self.caminho))]
            return lista
        else:
            return []
            
    def funcaoObjetivo(self):
        """
        Este método verifica se o caminho está no estado objetivo
        """

        #verifica se é uma pasta
        if os.path.isdir(self.caminho):
            return False
        else:#é um arquivo
            
            #separa o nome do arquivo do caminho
            indiceBarra = self.caminho.rfind(os.sep)
            nomeArquivo = self.caminho[indiceBarra + 1 :  ]
            
            if nomeArquivo == "f31.txt":
                return True
            else:
                return False        