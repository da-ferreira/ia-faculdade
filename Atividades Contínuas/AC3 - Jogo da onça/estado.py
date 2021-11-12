
from copy import deepcopy

class Estado:
    def __init__(self, tabuleiro=None):
        if tabuleiro is not None:
            self.tabuleiro = tabuleiro
        else:
            self.tabuleiro = self.estadoInicial()

    def estadoInicial(self):
        """ Retorna o estado inicial com o tabuleiro padrão. """
        return {
            '11': ['$', '12', '21', '22'],
            '12': ['$', '11', '13', '22'],
            '13': ['$', '12', '14', '22', '24'],
            '14': ['$', '13', '15', '24'],
            '15': ['$', '14', '25', '24',],
            '21': ['$', '11', '31', '22'],
            '22': ['$', '21', '11', '12', '13', '23', '31', '32', '33'],
            '23': ['$', '22', '13', '24', '33'],
            '24': ['$', '23', '25', '13', '14', '15', '33', '34', '35'],
            '25': ['$', '15', '35', '24'],
            '31': ['$', '21', '22', '32', '41', '42',],
            '32': ['$', '31', '33', '22', '42',],
            '33': ['C', '22', '23', '24', '32', '34', '42', '43', '44'],
            '34': ['$', '33', '35', '24', '44', ],
            '35': ['$', '25', '45', '34', '24', '44'],
            '41': ['o', '42', '31', '51'],
            '42': ['o', '41', '43', '31', '32', '33', '51', '52', '53'],
            '43': ['o', '42', '44', '33', '53'],
            '44': ['o', '43', '45', '33', '34', '35', '53', '54', '55'],
            '45': ['o', '44', '35', '55'],
            '51': ['o', '41', '42', '52'],
            '52': ['o', '51', '53', '42',],
            '53': ['o', '52', '54', '42', '43', '44', '62', '63', '64'],
            '54': ['o', '53', '55', '44'],
            '55': ['o', '54', '44', '45'],
            '62': ['o', '53', '71', '63'],
            '63': ['o', '62', '64', '53', '73'],
            '64': ['o', '63', '53', '75',],
            '71': ['o', '73', '62'],
            '73': ['o', '71', '75', '63'],
            '75': ['o', '73', '64']
        }  

    def funcaoSucessora(self, jogador=0):
        """
        Retorna todo os possiveis lugares que podem ser alcançados a partir do estado atual.
        jogador 0 é cachorro e 1 é onça.
        """

        estados = []

        if jogador == 0:  # Cachorro
            posicoes_cachorros = self.pegaPosicoesCachorros()
            
            for i in posicoes_cachorros:
                for j in self.tabuleiro[i][1:]:
                    if self.tabuleiro[j][0] == 'o':
                        novoTabuleiro = deepcopy(self.tabuleiro)
                        
                        novoTabuleiro[i][0] = 'o'
                        novoTabuleiro[j][0] = '$'
                        
                        estados.append(novoTabuleiro)

        else:  # Onça
            estado = self.pegaPosicaoOnca()
            posicoes_onca = [posicao for posicao in self.tabuleiro[estado][1:] if self.tabuleiro[posicao][0] in 'o$']
            
            for position in posicoes_onca:
                novoTabuleiro = deepcopy(self.tabuleiro)
                
                if novoTabuleiro[position][0] == '$':
                    proxima_casa = self._proximaCasa(estado, position)

                    if proxima_casa is not None and self.tabuleiro[proxima_casa][0] == 'o':
                        novoTabuleiro[estado][0] = 'o'
                        novoTabuleiro[position][0] = 'o'
                        novoTabuleiro[proxima_casa][0] = 'C'

                        estados.append(novoTabuleiro)
                else:
                    novoTabuleiro[estado][0] = 'o'
                    novoTabuleiro[position][0] = 'C'
                    estados.append(novoTabuleiro)

        return estados                    

    def funcaoObjetivo(self):
        """ Verifica se está no estado objetivo, ou seja, se venceu o jogo. """
        return self.cachorrosVenceram() or self.oncaVenceu()

    def _proximaCasa(self, onca, cachorro):
        """ Retorna a proxima casa da onça quando seu vizinho for um cachorro. """

        if onca in ['62', '64', '71', '75'] and onca[0] == cachorro[0]:
            if onca == '62':
                return '64'
            
            if onca == '62':
                return '62'

            if onca == '71':
                return '75'
            
            if onca == '75':
                return '71'

        onca = [int(onca[0]), int(onca[1])]
        cachorro = [int(cachorro[0]), int(cachorro[1])]

        if onca[0] == cachorro[0] and onca[1] < cachorro[1] and onca[1] < 4:  # Estão na mesma linha e cachorro ta na frente
            return str(onca[0]) + str(onca[1] + 2)
        
        if onca[0] == cachorro[0] and onca[1] > cachorro[1] and onca[1] > 2:  # Estão na mesma linha e cachorro ta na atras
            return str(onca[0]) + str(onca[1] - 2)

        if onca[1] == cachorro[1] and onca[0] > cachorro[0] and onca[0] > 2:  # Estão na mesma coluna e cachorro ta em cima
            return str(onca[0] - 2) + str(onca[1])

        if onca[1] == cachorro[1] and onca[0] < cachorro[0] and onca[0] < 6:  # Estão na mesma coluna e cachorro ta em baixo
            return str(onca[0] + 2) + str(onca[1])

        if ((onca[0] - 1) == cachorro[0]) and ((onca[1] - 1) == cachorro[1]) and (onca[0] > 2 and onca[1] > 2):  # Diagonal esquerda pra cima
            return str(onca[0] - 2) + str(onca[1] - 2)

        if ((onca[0] - 1) == cachorro[0]) and ((onca[1] + 1) == cachorro[1]) and (onca[0] > 2 and onca[1] < 4):  # Diagonal direita pra cima
            return str(onca[0] - 2) + str(onca[1] - 2)

        if ((onca[0] + 1) == cachorro[0]) and ((onca[1] - 1) == cachorro[1]) and (onca[0] < 4 and onca[1] > 2):  # Diagonal esquerda pra baixo
            return str(onca[0] + 2) + str(onca[1] - 2)
        
        if ((onca[0] + 1) == cachorro[0]) and ((onca[1] + 1) == cachorro[1]) and (onca[0] < 4 and onca[1] > 2):  # Diagonal direita pra baixo
            return str(onca[0] + 2) + str(onca[1] + 2)

        return None
            
    def pegaPosicoesCachorros(self):
        posicoes = []
        chaves = list(self.tabuleiro.keys())

        for i in chaves:
            if self.tabuleiro[i][0] == "$":
                posicoes.append(i)
        
        return posicoes

    def pegaPosicaoOnca(self):
        chaves = list(self.tabuleiro.keys())

        for i in chaves:
            if self.tabuleiro[i][0] == "C":
                return i
                
    def cachorrosVenceram(self):
        onca = self.pegaPosicaoOnca()
        vizinhos_onca = self.tabuleiro[onca][1:]
        posicoes_de_fuga_onca = []

        for i in vizinhos_onca:
            if self.tabuleiro[i][0] == 'o':
                return False

        for i in vizinhos_onca:
            if self.tabuleiro[i][0] == "$":     
                temp = self._proximaCasa(onca, i)
                if temp is not None and self.tabuleiro[temp][0] == 'o' :
                    posicoes_de_fuga_onca.append(temp)
                
        return len(posicoes_de_fuga_onca) == 0        

    def oncaVenceu(self):
        numero_cachorros = self.pegaPosicoesCachorros()
        return len(numero_cachorros) <= 9
            

if __name__ == "__main__":
    estado = Estado()
    
    #estado.tabuleiro['33'][0] = 'o'
    #estado.tabuleiro['11'][0] = 'C'
    #estado.tabuleiro['31'][0] = 'o'
    #estado.tabuleiro['34'][0] = 'o'
    #estado.tabuleiro['44'][0] = '$'
    
    #print(estado.tabuleiro['44'])
    
    #print(estado.funcaoSucessora('', 0))
    print(len(estado.funcaoSucessora(1)))

    #print(estado.funcaoObjetivo())