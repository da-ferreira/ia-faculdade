
import random
from deap import base, creator, tools

import matplotlib.pyplot as plt
import seaborn as sns

#constantes do problema:
TAMANHO_ONE_MAX = 600     # tamanho da string

#constantes do algoritmo genético:
TAMANHO_POPULACAO = 200    #tamanho da populacao
P_CROSSOVER = 0.9          #probabilidade de crossover
P_MUTACAO = 0.1            #probabilidade de mutacao em um individuo
                       
MAX_GERACAO = 600     # numero maximo de geracoes

#inicia a toolbox                         
toolbox = base.Toolbox()

creator.create("FitnessMax", base.Fitness, weights=(1.0,))

creator.create("Individual",list, fitness=creator.FitnessMax)

#o operador zero_ou_um retornara aleatoriamente o valor 0 ou o valor 1
toolbox.register("zero_ou_um", random.randint, 0, 1)

toolbox.register("individualCreator", tools.initRepeat, 
        creator.Individual, toolbox.zero_ou_um, TAMANHO_ONE_MAX)

#seed do gerador de numeros aleatorios 
RANDOM_SEED = 7
#random.seed(RANDOM_SEED)

#define a populacao como uma lista de indivíduos
toolbox.register("populationCreator", tools.initRepeat, 
                 list, toolbox.individualCreator)

#funcao de avaliacao
def func_avaliacao(individual):
    #target_sum = 45
    return sum(individual), # returna uma tupla

#cadastra o operador de avaliação 
toolbox.register("evaluate", func_avaliacao)

#define o operador de crossover
toolbox.register("acasalar", tools.cxTwoPoint)

#define  um operador de mutação
toolbox.register("mutacao", tools.mutFlipBit, indpb=1.0/TAMANHO_ONE_MAX)

#define um operador para selecionar individuos para reprodução
toolbox.register("seleciona", tools.selTournament, tournsize=2)


#algoritmo Genetico:
def main():

    #cria populacao inicial (geracao 0):
    population = toolbox.populationCreator(n=TAMANHO_POPULACAO)
    contadorDeGeracao = 0

    #calcula tupla de aptidão para cada indivíduo na população: 
    valoresFitness = list(map(toolbox.evaluate, population))
    for individual, fitnessValue in zip(population, valoresFitness):
        individual.fitness.values = fitnessValue

    #extrair valores de aptidao de todos os individuos na populacao:
    valoresFitness = [individual.fitness.values[0] for individual in population]

    #inicializar acumuladores de estatísticas:
    maxValoresFitness = []
    valoresFitnessMedios = []

    #ciclo evolutivo principal:
    #pare se o valor máximo de eficiencia (fitness) for atingido
    #OU se o número de gerações exceder o valor predefinido:
    while max(valoresFitness) < TAMANHO_ONE_MAX and contadorDeGeracao < MAX_GERACAO:
        #contador de atualizacoo:
        contadorDeGeracao +=  1

        #aplica o operador de seleção, para selecionar os indivíduos da próxima geração:
        prole = toolbox.seleciona(population, len(population))

        #clona os individuos selecionados: 
        prole = list(map(toolbox.clone, prole))

        #aplique o operador crossover a pares de descendentes:
        for filho1, filho2 in zip(prole[::2], prole[1::2]):
            if random.random() < P_CROSSOVER:
                toolbox.acasalar(filho1, filho2)
                del filho1.fitness.values
                del filho2.fitness.values

        for mutante in prole:
            if random.random() < P_MUTACAO:
                toolbox.mutacao(mutante)
                del mutante.fitness.values

        #calcula a aptidao para os individuos sem nenhum valor de aptidao calculado 
        # anterior:
        individuosNovos = [ind for ind in prole if not ind.fitness.valid]
        novoValoresFitness = list(map(toolbox.evaluate, individuosNovos))
        for individual, ValorFitness in zip(individuosNovos, novoValoresFitness):
            individual.fitness.values = ValorFitness

        #troca apopulacao pela nova prole:
        population[:] = prole

        #coleta valores de fitness em uma lista, atualiza as estatísticas e imprime:
        valoresFitness = [ind.fitness.values[0] for ind in population]

        maxFitness = max(valoresFitness)
        fitnessMedio = sum(valoresFitness) / len(population)
        maxValoresFitness.append(maxFitness)
        valoresFitnessMedios.append(fitnessMedio)
        print("- Geração {}: Max Fitness = {}, Fitness Media = {}".format(contadorDeGeracao, maxFitness, fitnessMedio))

        # Encontre e imprima o melhor indivíduo:
        #indice_melhor = valoresFitness.index(max(valoresFitness))
        #print("Melhor Individuo = ", *population[indice_melhor], "\n")
    
    sns.set_style("whitegrid")
    plt.plot(maxValoresFitness, color='red', label='Fitness Máxima')
    plt.plot(valoresFitnessMedios, color='green', label='Média fitness')
    plt.xlabel('Gerações')
    plt.ylabel('Fitness Máxima / Média')
    plt.title('Fitness máxima e média ao longo das gerações')

    plt.legend(fontsize=12, loc=4)
    plt.show()


if __name__ == '__main__':
    main()
