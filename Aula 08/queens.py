
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class NQueens:
    """
    Esta classe encapsula o problema das N-Queens
    """

    def __init__(self, nrQueens):
        self.nrQueens = nrQueens

    def __len__(self):
        """
        :return: numero de rainhas
        """
        return self.nrQueens

    def getNumeroDeViolacao(self, posicoes):
        """
         Calcula o numero de violacoes na solucao dada
         Uma vez que a entrada contem indices exclusivos de colunas para cada linha, 
        nenhuma violacao de linha ou coluna eh possível,
         Apenas as violacoes diagonais precisam ser contadas.
        """

        violacao = 0

        # itera sobre cada par de rainhas e descubra se eles estão na mesma diagonal:
        for i in range(len(posicoes)):
            for j in range(i + 1, len(posicoes)):

                # primeiro par de rainhas:
                coluna1 = i
                linha1 = posicoes[i]

                # segundo par de rainhas:
                coluna2 = j
                linha2 = posicoes[j]

                # procura a ameaça diagonal para o par atual:
                if abs(coluna1 - coluna2) == abs(linha1 - linha2):
                    violacao += 1

        return violacao 

    def desenhaTabuleiro(self, posicoes):
        """
        Desenha as posicoes das rainhas no tabuleiro de acordo com a solucao dada
        """

        fig, ax = plt.subplots()

        # comeca com os quadrados do tabuleiro:
        tabuleiro = np.zeros((self.nrQueens, self.nrQueens))
        # muda a cor de todos os outros quadrados:
        tabuleiro[::2, 1::2] = 1
        tabuleiro[1::2, ::2] = 1

        # desenhe os quadrados com duas cores diferentes:
        ax.imshow(tabuleiro, interpolation='none', cmap=mpl.colors.ListedColormap(['#ffc794', '#4c2f27']))

        # leia a miniatura da imagem da rainha e da uma margem de 70% das dimensoes do quadrado:
        queenThumbnail = plt.imread('C:/Users/Home/Desktop/CC - 4°/Inteligência Artificial/IA Algoritmos/Aula 08/queen-thumbnail.png')
        thumbnailSpread = 0.70 * np.array([-1, 1, -1, 1]) / 2  

        # itera sobre as posições da rainha (i é a linha, j é a coluna):
        for i, j in enumerate(posicoes):
            # coloca a miniatura no quadrado correspondente:
            ax.imshow(queenThumbnail, extent=[j, j, i, i] + thumbnailSpread)

        # mostr os Indices de linha e coluna:
        ax.set(xticks=list(range(self.nrQueens)), yticks=list(range(self.nrQueens)))

        ax.axis('image') 

        return plt


# testa a classe:
def main():
    # cria uma instancia do problema:
    nQueens = NQueens(8)

    # uma solucao boa:
    #solucao = [5, 0, 4, 1, 7, 2, 6, 3]

    # uma solucao com 3 violacoes:
    solucao = [1, 2, 7, 5, 0, 3, 4, 6]

    print("Numero de violacoes = ", nQueens.getNumeroDeViolacao(solucao))

    plot = nQueens.desenhaTabuleiro(solucao)
    plot.show()


if __name__ == "__main__":
    main()