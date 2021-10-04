
import random
from deap import base, tools

RANDOM_SEED = 74
#random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

toolbox.register("zero_ou_um", random.randint, 0, 1)

randomList = tools.initRepeat(list, toolbox.zero_ou_um, 100)

print(randomList)
 