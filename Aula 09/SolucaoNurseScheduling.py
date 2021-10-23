
from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import random
from deap.tools.support import Statistics
import numpy

import matplotlib.pyplot as plt
import seaborn as sns

import elitism
import nurse


PENALIDADE_HARD_CONSTRAINT = 10  # Fator de penalidade para uma violação Hard

# Parametros para o Algoritmo Genetico
TAMANHO_DA_POPULACAO = 400
P_CROSSOVER = 0.9  # Probabilidade de crossover
P_MUTACAO = 0.1    # Probabilidade de mutacao em um individuo
NR_MAX_GERACOES = 250
TAMANHO_HALL_OF_FAME = 40

# Seleciona uma random seed:
RANDOM_SEED = 100
#random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

# Cria uma instancia do nurse scheduling problem
nsp = nurse.NurseSchedulingProblem(PENALIDADE_HARD_CONSTRAINT)

# Define a estrategia da funcao Fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# Cria uma classe Individual sub-classe de list:
creator.create("Individual", list, fitness=creator.FitnessMin)

# Cria uma funcao para gerar 0's e 1's
toolbox.register("zeroOuUm", random.randint, 0, 1)

# Cria um operador para preencher uma instância da classe Individual:
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOuUm, len(nsp))

# Cria a funcao populacaooperator para gerar uma lista de objetos Individual
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# Calculo do valor fitness
def calculaCusto(individual):
    return nsp.calculaCusto(individual),  # returna uma tupla


toolbox.register("evaluate", calculaCusto)

# Operadores geneticos
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/len(nsp))

# Algoritmo Genetico:
def main():

    # Cria populacao inicial (geracao 0)
    populacao = toolbox.populationCreator(n=TAMANHO_DA_POPULACAO)

    # Prepara o objeto estatisticas
    estatisticas = tools.Statistics(lambda ind: ind.fitness.values)
    estatisticas.register("min", numpy.min)
    estatisticas.register("med", numpy.mean)

    # Define o objeto hall-of-fame
    hof = tools.HallOfFame(TAMANHO_HALL_OF_FAME)

    # Executa um algoritmo genetico da biblioteca
    
    #populacao, logbook = algorithms.eaSimple(populacao, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTACAO,
    #                                          ngen=NR_MAX_GERACOES, stats=estatisticas, halloffame=hof, verbose=True)


    populacao, logbook = elitism.eaSimpleWithElitism(populacao, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTACAO,
                                                     ngen=NR_MAX_GERACOES, stats=estatisticas, halloffame=hof, verbose=True)

    # Print da solucao encontrada
    melhor = hof.items[0]

    print("-- Melhor Individuo: ", melhor)
    print("-- Melhor Fitness: ", melhor.fitness.values[0])
    
    print()
    
    print("-- Schedule -- ")
    nsp.printScheduleInfo(melhor)

    # Extrai as estatisticas:
    menoresValoresFitnes, valoresFitnessMedios = logbook.select("min", "med")

    # Grafico com as estatisticas:
    sns.set_style("whitegrid")
    plt.plot(menoresValoresFitnes, color='red', label='Menores fitness')
    plt.plot(valoresFitnessMedios, color='green', label='Fitness médios')
    plt.xlabel('Gerações')
    plt.ylabel('Fitness Mínima / Media')
    plt.title('Fitness mínima e média através das gerações')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
     