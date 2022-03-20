from random import choices, random, seed
from numpy import *
import pyperclip
seed2Use = pyperclip.paste()
print(seed2Use)
seed(seed2Use)

# ####################################################
# 1
# Mutation Functions


# 1.1 mutations rates loaded from file
def mutationRate(child, index, incomprate, stepMut):
    freqs = [incomprate * stepMut ** 5, incomprate * stepMut ** 4, incomprate * stepMut ** 3,
                      incomprate * stepMut ** 2, incomprate * stepMut, incomprate, 0]
    freqs[6] = 1 - sum(freqs)

    mutation_steps = choices([6, 5, 4, 3, 2, 1, 0], freqs, k=1)
    mutation_step = mutation(mutation_steps[0])
    child[index] = child[index] + mutation_step

    return child, mutation_step

# 1.2 mutations forced on each duo/trio
def mutation(step):
    addorsubtract = 2 * choices([0, 1], k=1)[0] - 1
    return step * addorsubtract

# ####################################################
# 2
# Create child and insert mutations

# 2.1 generates child (2 alleles) given a father and a mother
# father (and mother) may have one or two alleles
def childof(father, mother):
    child = [0, 0]
    child[0] = choices(father, k=1)[0]
    child[1] = choices(mother, k=1)[0]
    return child

# 2.2 add mutation generated at #1
def mutationchild(child, mutation_step, index):
    if isinstance(mutation_step, list):
        print("mutation_step: ", mutation_step, " index: ", index)
        child[0] = child[0] + mutation_step[0]
        child[1] = child[1] + mutation_step[1]
    else:
        child[index] = child[index] + mutation_step

    return child


# ####################################################
# 3
# Generate Families

# 3.1b autossomes
def genFamilies_v2(alleles, frequencies, mutStepMale=1, mutStepFemale=1, rThresh=0.5):
    father = choices(alleles, frequencies, k=2)
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    randVal = random.random()

    if rThresh > 1: # mutation at both alleles
        mutation_step = [mutation(mutStepMale), mutation(mutStepFemale)]
        index = [0, 1]

    else:

        if randVal >= rThresh:
            index = 0
            mutation_step = mutation(mutStepMale)
        else:
            index = 1
            mutation_step = mutation(mutStepFemale)

    return father, mother, child, mutation_step, index
