
from estado import Estado

class No:
    def __init__(self, estado):
        self.estado = estado

    def printTabuleiro(self):
        print(f"A    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(5)])}")
        print("     | \ | / | \ | / |")
        print(f"B    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(5, 10)])}")
        print("     | / | \ | / | \ |")
        print(f"C    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(10, 15)])}")
        print("     | \ | / | \ | / |")
        print(f"D    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(15, 20)])}")
        print("     | / | \ | / | \ |")
        print(f"E    {' - '.join([self.estado.tabuleiro[list(self.estado.tabuleiro.keys())[i]][0] for i in range(20, 25)])}")
        print("            /|\\")
        print("           / | \\")
        print("          /  |  \\")
        print(f"F        {self.estado.tabuleiro['f2'][0]} - {self.estado.tabuleiro['f3'][0]} - {self.estado.tabuleiro['f4'][0]}")
        print("        /    |    \\")
        print("       /     |     \\")
        print("      /      |      \\")
        print(f"G    {self.estado.tabuleiro['g1'][0]} ----- {self.estado.tabuleiro['g3'][0]} ----- {self.estado.tabuleiro['g5'][0]}")
        print("     1   2   3   4   5")
     
    def heuristica(self):
        """ Calcula a função heuristica para a onça. """
        pass
    
if __name__ == "__main__":
    no = No(Estado())
    no.printTabuleiro()