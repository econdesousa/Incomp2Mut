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


def distexcludezero(num1, num2):
    if max([num1, num2]) > 0:
        return min(x for x in [num1, num2] if x > 0)
    else:
        return 0


def countincomp(child, father=0, mother=0):
    if father == 0 and mother == 0:
        exit("no father, no mother, nothing to do")

    if len(child) == 2:  # (autossomes or X chrom for female child)
        if father == 0:  # No father available
            if mother != 0:
                A = 0
                B = alleledist(child[1], mother)
                C = 0
                D = alleledist(child[0], mother)
            else:
                exit("no father, no mother, nothing to do")
        elif mother == 0:  # No mother available
            if father != 0:
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

    elif len(child) == 1:  # male X chrom
        if father != 0:
            print("###########################################")
            print("###########################################")
            print("###########################################")
            print("Child -> male")
            print("X chromossome")
            print("Father shouldn't be available: line 107")
            print("###########################################")
            print("###########################################")
            print("###########################################")

        A = 0

        if mother != 0:
            D = alleledist(child[0], mother)
        else:
            print("###########################################")
            print("###########################################")
            print("###########################################")
            print("Child -> male")
            print("X chromossome")
            print("Father shouldn't be available: line 122")
            print("Father and Mother: both missing")
            print("###########################################")
            print("###########################################")
            print("###########################################")
            D = 0

        return [A, D]

    else:
        exit("len(child) out of bounds")
