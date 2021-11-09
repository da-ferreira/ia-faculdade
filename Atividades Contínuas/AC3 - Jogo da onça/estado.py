
class Estado:
    def __init__(self, tabuleiro=None):
        if tabuleiro is not None:
            self.tabuleiro = tabuleiro
        else:
            self.tabuleiro = self.estadoInicial()

    def estadoInicial(self):
        """ Retorna o estado inicial com o tabuleiro padrão. """
        return {
            'a1': ['$', 'a2', 'b1', 'b2'],
            'a2': ['$', 'a1', 'a3', 'b2'],
            'a3': ['$', 'a2', 'a4', 'b2', 'b4'],
            'a4': ['$', 'a3', 'a5', 'b4'],
            'a5': ['$', 'a4', 'b5', 'b4',],
            'b1': ['$', 'a1', 'c1', 'b2'],
            'b2': ['$', 'b1', 'a1', 'a2', 'a3', 'b3', 'c1', 'c2', 'c3'],
            'b3': ['$', 'b2', 'a3', 'b4', 'c3'],
            'b4': ['$', 'b3', 'b5', 'a3', 'a4', 'a5', 'c3', 'c4', 'c5'],
            'b5': ['$', 'a5', 'c5', 'b4'],
            'c1': ['$', 'b1', 'b2', 'c2', 'd1', 'd2',],
            'c2': ['$', 'c1', 'c3', 'b2', 'd2',],
            'c3': ['C', 'b2', 'b3', 'b4', 'c2', 'c4', 'd2', 'd3', 'd4'],
            'c4': ['$', 'c3', 'c5', 'b4', 'd4', ],
            'c5': ['$', 'b5', 'd5', 'c4', 'b4', 'd4'],
            'd1': ['o', 'd2', 'c1', 'e1'],
            'd2': ['o', 'd1', 'd3', 'c1', 'c2', 'c3', 'e1', 'e2', 'e3'],
            'd3': ['o', 'd2', 'd4', 'c3', 'e3'],
            'd4': ['o', 'd3', 'd5', 'c3', 'c4', 'c5', 'e3', 'e4', 'e5'],
            'd5': ['o', 'd4', 'c5', 'e5'],
            'e1': ['o', 'd1', 'd2', 'e2'],
            'e2': ['o', 'e1', 'e3', 'd2',],
            'e3': ['o', 'e2', 'e4', 'd2', 'd3', 'd4', 'f2', 'f3', 'f4'],
            'e4': ['o', 'e3', 'e5', 'd4'],
            'e5': ['o', 'e4', 'd4', 'd5'],
            'f2': ['o', 'e3', 'g1', 'f3'],
            'f3': ['o', 'f2', 'f4', 'e3', 'g3'],
            'f4': ['o', 'f3', 'e3', 'g5',],
            'g1': ['o', 'g3', 'f2'],
            'g3': ['o', 'g1', 'g5', 'f3'],
            'g5': ['o', 'g3', 'f4'],
        }  

    def funcaoSucessora(self, estado, jogador=0):
        """
        Retorna todo os possiveis lugares que podem ser alcançados a partir do estado atual.
        jogador 0 é cachorro e 1 é onça.
        """

        estados = []

        if jogador == 0:  # Cachorro
            posicoes_cachorros = [posicao for posicao in self.tabuleiro[estado][1:] if self.tabuleiro[posicao][0] == 'o']
        else:  # Onça
            pass

    def funcaoObjetivo(self):
        """ Verifica se está no estado objetivo, ou seja, se venceu o jogo. """
        return self.cachorrosVenceram() or self.oncaVenceu()

if __name__ == "__main__":
    estado = Estado()
    estado.tabuleiro['c3'][0] = 'o'
    estado.tabuleiro['d3'][0] = 'C'
    estado.tabuleiro['c4'][0] = 'o'
    estado.tabuleiro['d4'][0] = '$'
    print(estado.funcaoSucessora('d3', 1))