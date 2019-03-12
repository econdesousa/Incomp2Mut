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



def  countincomp(child, father=0, mother=0):
    ## hipotesis:
    # CHILD has lenght 1 or 2 (male X chrom or autossomes)
    # FATHER has lenght 1 or 2 (X chrom or autossomes)
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

    if len(child)==2: #(autossomes or X chrom for female child)
        if father == 0: #No father available
            if mother != 0: # redundancy
                A = 0
                B = alleledist(child[1], mother)
                C = 0
                D = alleledist(child[0], mother)
            else:
                exit("no father, no mother, nothing to do")
        elif mother == 0: #No mother available
            if father != 0: # redundancy
                A = alleledist(child[0], father)
                B = 0
                C = alleledist(child[1], father)
                D = 0
            else:
                exit("no father, no mother, nothing to do")
        elif father != 0 and mother != 0:
            A = alleledist(child[0], father)
            B = alleledist(child[1], mother)
            C = alleledist(child[1], father)
            D = alleledist(child[0], mother)
        else:
            exit("Unpredicted case")

        if A + B > C + D:
            return [C, D]
        elif A + B == C + D:
            if min([A, B]) < min([C, D]):
                return [A, B]
            else:
                return [C, D]
        else:
            return [A, B]

    elif len(child)==1: # male X chrom
        if len(father) != 0: # shouldn't occur
            print("###########################################")
            print("###########################################")
            print("###########################################")
            print("Child -> male")
            print("X chromossome")
            print("Father shouldn't be available")
            print("###########################################")
            print("###########################################")
            print("###########################################")

        A=0

        if len(mother) != 0:
            D = alleledist(child[0], mother)
        else: # shouldn't occur
            print("###########################################")
            print("###########################################")
            print("###########################################")
            print("Child -> male")
            print("X chromossome")
            print("Father shouldn't be available")
            print("Father and Mother: both missing")
            print("###########################################")
            print("###########################################")
            print("###########################################")
            D = 0

        return [A, D]

    else:
        exit("len(child) out of bounds")




def countincomp_old(child, father=0, mother=0):
    if father != 0:
        A = alleledist(child[0], father)
        if len(child) > 1:
            C = alleledist(child[1], father)
        else:
            C = 0
    else:
        A = 0
        C = 0
    if mother != 0:
        if len(child)>1:
            B = alleledist(child[1], mother)
        else:
            B = 0
        D = alleledist(child[0], mother)
    else:
        B = 0
        D = 0

    if len(child) == 1:
        if A<D:
            return [A, 0]
        else:
            return [0, D]
    elif A + B > C + D:
        return [C, D]
    elif A + B == C + D:
        if min([A, B]) < min([C, D]):
            return [A, B]
        else:
            return [C, D]
    else:
        return [A, B]


