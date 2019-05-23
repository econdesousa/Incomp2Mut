from random import choices, seed
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
    child[index] = child[index] + mutation_step
    return child


# ####################################################
# 3
# Generate Families

# 3.1 autossomes
def genFamilies(alleles, frequencies, mutStep=1):
    father = choices(alleles, frequencies, k=2)
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    index = choices([0, 1], k=1)[0]
    mutation_step = mutation(mutStep)
    return father, mother, child, mutation_step, index

# 3.2 X chromossome and female child
def genFamiliesXdaughter(alleles, frequencies, mutStep=1):
    father = choices(alleles, frequencies, k=1)  # father has one allele
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    index = choices([0, 1], k=1)[0]
    mutation_step = mutation(mutStep)
    return father, mother, child, mutation_step, index

# 3.1 X chromossome and male child
def genFamiliesXson(alleles, frequencies, mutStep=1):
    father = choices(alleles, frequencies, k=2)
    father = [father[0]]
    mother = choices(alleles, frequencies, k=2)

    child = childof(father, mother)
    child = [child[1]]  # child has just one allele.
    # To allow us to use func childof, two alleles are generated and one is then removed
    index = 0 #just one allele, thus index must be 0
    mutation_step = mutation(mutStep)
    return father, mother, child, mutation_step, index