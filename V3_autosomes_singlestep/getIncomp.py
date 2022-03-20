import math


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def numIntersect(lst1, lst2):
    lst3 = intersection(lst1, lst2)
    return len(lst3)


def belongsto(num, lst1):
    ans = 0
    for value in lst1:
        if num == value:
            ans = 1
            break
    return ans


def alleledist(allele, lst1):
    lst2 = [abs(math.trunc(10*x - 10*allele)/10) for x in lst1]
    for it in range(len(lst2)):
        if lst2[it] != math.trunc(lst2[it]):
            lst2[it] = math.trunc(lst2[it]) + 1000
    return min(lst2)


#only works for values >=0
def distexcludezero(num1, num2):
    if max([num1, num2]) > 0:
        return min(x for x in [num1, num2] if x > 0)
    else:
        return 0


def  countincomp_v2(child, father=0, mother=0):
    ## hypothesis:
    # CHILD has length 1 or 2 (male X chrom or autosomes)
    # FATHER has length 1 or 2 (X chrom or autosomes)
    # MOTHER has length 2
    # FATHER or MOTHER are missing (duos)

    # Variables 2 create:
    #       A: alleledist(child[0], father)
    #       B: alleledist(child[1], mother)
    #       C: alleledist(child[1], father)
    #       D: alleledist(child[0], mother)
    # rationale :
    # CHILD=[FATHER[i] + mut[1], MOTHER[j] + mut[2]] or CHILD=[MOTHER[j] + mut[1], FATHER[i] + mut[2]],
    # for i,j in [0,1]

    # Bifurcations:
    #           len(CHILD)

    if father == 0 and mother == 0:
        exit("no father, no mother, nothing to do")

    if father == 0:
        father = [float('inf'), float('inf')]

    if mother == 0:
        mother = [float('inf'), float('inf')]

    if len(child) == 1:
        child = [child[0], float('inf')]

    if len(father) == 1:
        father = [father[0], float('inf')]

    if len(mother) == 1:  # shouldn't occur (y chrom not tested here)
        mother = [mother[0], float('inf')]
        print("###########################################")
        print("###########################################")
        print("###########################################")
        print("Mother with just one allele")
        print("Check what happens")
        print("###########################################")
        print("###########################################")
        print("###########################################")

    child1=[child[1], child[0]]
    return [dist2Vecs([father[0], mother[0]], child),  dist2Vecs([father[0], mother[1]], child),
            dist2Vecs([father[1], mother[0]], child),  dist2Vecs([father[1], mother[1]], child),
            dist2Vecs([father[0], mother[0]], child1), dist2Vecs([father[0], mother[1]], child1),
            dist2Vecs([father[1], mother[0]], child1), dist2Vecs([father[1], mother[1]], child1)]


# auxiliary function (called just from countincomp_v2
def dist2Vecs(vec1, vec2):
    return [abs(vec1[0] - vec2[0]), abs(vec1[1] - vec2[1])]


"""
father=[10,10]
mother=[12,11]
child=[12,11]
vec=countincomp_v2(child, father, mother)
print(vec)
for i in range(len(vec)):
    for j in range(len(vec[0])):
        print(vec[i][j],end="\t")
print(float('inf'))
"""

