from random import choices, seed
from numpy import *
seed(9001)


def mutation(step):
    addorsubtract = 2 * choices([0, 1], k=1)[0] - 1
    return step * addorsubtract


def childof(father, mother):
    child = [0, 0]
    child[0] = choices(father, k=1)[0]
    child[1] = choices(mother, k=1)[0]
    return child


def mutationchild(child, mutation_step, index):
    child[index] = child[index] + mutation_step
    return child


def genFamilies(alleles, frequencies, mutStep=1):
    father = choices(alleles, frequencies, k=2)
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    index = choices([0, 1], k=1)[0]
    mutation_step = mutation(mutStep)
    return father, mother, child, mutation_step, index


def genFamiliesXdaughter(alleles, frequencies, mutStep=1):
    father = choices(alleles, frequencies, k=2)
    father = [father[0]]
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    index = choices([0, 1], k=1)[0]
    mutation_step = mutation(mutStep)
    return father, mother, child, mutation_step, index

def genFamiliesXson(alleles, frequencies, mutStep=1):
    father = choices(alleles, frequencies, k=2)
    father[0] = father[1]
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    child = [child[1]]
    index = 1
    mutation_step = mutation(mutStep)
    return father, mother, child, mutation_step, index


def mutationRate_old(child, index, incomprate, stepMut):
    mutation_steps = [incomprate*stepMut**5, incomprate*stepMut**4, incomprate*stepMut**3, incomprate*stepMut**2, incomprate*stepMut, incomprate, 1]
    mutation_steps[6] = 1 - (incomprate*stepMut**4 + incomprate*stepMut**3 + incomprate*stepMut**2 + incomprate*stepMut + incomprate)
    mutation_step_sum = cumsum(mutation_steps)
    r = random.uniform(0,1)
    if r < mutation_step_sum[0]:
        mutation_steps = 6
    elif r < mutation_step_sum[1]:
        mutation_steps = 5
    elif r < mutation_step_sum[2]:
        mutation_steps = 4
    elif r < mutation_step_sum[3]:
        mutation_steps = 3
    elif r < mutation_step_sum[4]:
        mutation_steps = 2
    elif r < mutation_step_sum[5]:
        mutation_steps = 1
    elif r < mutation_step_sum[6]:
        mutation_steps = 0
    else:
        exit("mutation rates out of bounds")

    mutation_step = mutation(mutation_steps)
    child[index] = child[index] + mutation_step

    return child, mutation_step


def mutationRate(child, index, incomprate, stepMut):
    freqs = [incomprate * stepMut ** 5, incomprate * stepMut ** 4, incomprate * stepMut ** 3,
                      incomprate * stepMut ** 2, incomprate * stepMut, incomprate, 0]
    freqs[6] = 1 - sum(freqs)

    mutation_steps = choices([6, 5, 4, 3, 2, 1, 0], freqs, k=1)
    mutation_step = mutation(mutation_steps[0])
    child[index] = child[index] + mutation_step

    return child, mutation_step


