
from estado import Estado

class No:
    def __init__(self, estado):
        self.estado = estado

    def printTabuleiro(self):
        print(f"1    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(5)])}")
        print("     | \ | / | \ | / |")
        print(f"2    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(5, 10)])}")
        print("     | / | \ | / | \ |")
        print(f"3    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(10, 15)])}")
        print("     | \ | / | \ | / |")
        print(f"4    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(15, 20)])}")
        print("     | / | \ | / | \ |")
        print(f"5    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(20, 25)])}")
        print("            /|\\")
        print("           / | \\")
        print("          /  |  \\")
        print(f"6        {self.estado.tabuleiro['62'][0]} - {self.estado.tabuleiro['63'][0]} - {self.estado.tabuleiro['64'][0]}")
        print("        /    |    \\")
        print("       /     |     \\")
        print("      /      |      \\")
        print(f"7    {self.estado.tabuleiro['71'][0]} ----- {self.estado.tabuleiro['73'][0]} ----- {self.estado.tabuleiro['75'][0]}")
        print("     1   2   3   4   5")
     
    def heuristica(self, jogador=0):
        """
        Calcula a função heuristica para a onça e os cachorros.
        Se jogador for 1 a função heuristica é para a ONÇA, se for 0 é para os CACHORROS
        """
        
        heuristica = 0

        if jogador == 1:  # Onca
            # Calcula se ele comeu algum cachorro
            qtd_cachorros = len(self.estado.pegaPosicoesCachorros())

            if qtd_cachorros == 9:  # Venceu o jogo
                return -1000
            else:
                heuristica -= ((14 - qtd_cachorros) * 10)
            
            posicao_onca = self.estado.pegaPosicaoOnca()
            vizinhos_onca = self.estado.tabuleiro[posicao_onca][1:]

            tem_vizinho_vazio = False

            for i in vizinhos_onca:
                if self.estado.tabuleiro[i][0] == 'o':
                    heuristica -= 3            
                    tem_vizinho_vazio = True

            if not tem_vizinho_vazio:
                if self.estado.cachorrosVenceram():
                    heuristica = 1000

        else:  # Cachorros
            if self.estado.cachorrosVenceram():
                return 1000

            if self.estado.oncaVenceu():
                return -1000

            posicoes_cachorros = self.estado.pegaPosicoesCachorros()
            heuristica += len(posicoes_cachorros) * 3
            posicao_onca = self.estado.pegaPosicaoOnca()
            
            for i in posicoes_cachorros:
                if posicao_onca in self.estado.tabuleiro[i][1:]:
                    heuristica += 7

        return heuristica


    
if __name__ == "__main__":
    no = No(Estado())
    no.printTabuleiro()

    #no.estado.tabuleiro['33'][0] = 'o'
    #no.estado.tabuleiro['11'][0] = 'C'

    print(no.heuristica(1))