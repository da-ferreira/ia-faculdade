
from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import random
import array
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import elitism
import queens


NR_QUEENS = 10

# Constantes do algoritmo genetico:
TAMANH0_POPULACAO = 300
MAX_GENERACOES = 200
TAMANHO_HALL_OF_FAME = 30
P_CROSSOVER = 0.9  # probabilidade de  crossover
P_MUTATION = 0.1   # probabilidade de mutacao em um individuo

# >>>>> REMOVER <<<<<<
RANDOM_SEED = 42
#random.seed(RANDOM_SEED)

# cria o N-Queens desejado
nQueens = queens.NQueens(NR_QUEENS)
toolbox = base.Toolbox()

# define um único objetivo, minimizando a estratégia de fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# cria a classe individual com base na lista de inteiros
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

# cria um operador que gere indices aleatoriamente embaralhados
toolbox.register("randomOrder", random.sample, range(len(nQueens)), len(nQueens))

# cria o operador de criação individual para preencher uma instância 
#individual com índices embaralhados
toolbox.register("individualCreator", tools.initIterate,
                creator.Individual, toolbox.randomOrder)

# cria o operador de criacao de populacao para gerar uma lista de individuos
toolbox.register("polulacaoCreator", tools.initRepeat, list, toolbox.individualCreator)

# calculo de aptidão 
def totalViolacoes(individual):
    # retorna um tupla
    return nQueens.getNumeroDeViolacao(individual),
    
toolbox.register("evaluate", totalViolacoes)

# Operadores genéticos:
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxUniformPartialyMatched, indpb=2.0/len(nQueens))
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0/len(nQueens))

# Algoritmo Genetico
def main():
    # criar populacao inicial (geração 0):
    polulacao = toolbox.polulacaoCreator(n=TAMANH0_POPULACAO)

    # prepare o objeto de estatísticas:
    estatistica = tools.Statistics(lambda ind: ind.fitness.values)
    estatistica.register("min", np.min)
    estatistica.register("med", np.mean)

    # define oo objetos hall-of-fame:
    hof = tools.HallOfFame(TAMANHO_HALL_OF_FAME)

    polulacao, logbook = algorithms.eaSimple(polulacao, 
        toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
        ngen=MAX_GENERACOES, stats=estatistica, 
        halloffame=hof, verbose=True)

    # execute o fluxo do algoritmo genetico com o recurso hof adicionado:
    #polulacao, logbook = elitism.eaSimpleWithElitism(polulacao, 
    #        toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
    #        ngen=MAX_GENERACOES, stats=estatistica, 
    #        halloffame=hof, verbose=True)
    # print informacoe dos membor do hall da fama:
    
    print("- As melhores soluções são:")
    for i in range(TAMANHO_HALL_OF_FAME):
        print(i, ": ", hof.items[i].fitness.values[0], " -> ", hof.items[i])
        
    # Grafico com estatisticas:
    valoresMinimosDeFitness, valoresMediosDeFitness = logbook.select("min", "med")
    plt.figure(1)
    sns.set_style("whitegrid")
    plt.plot(valoresMinimosDeFitness, color='red', label='Fitness mínima')
    plt.plot(valoresMediosDeFitness, color='green', label='Média fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness Mínima / Média')
    plt.title('Fitness mínima e média ao longo das gerações')

    # desenha a melhor solucao:
    sns.set_style("whitegrid", {'axes.grid' : False})
    plt.legend(fontsize=12, loc=1)
    nQueens.desenhaTabuleiro(hof.items[0])
    plt.show()

if __name__ == "__main__":
    main()