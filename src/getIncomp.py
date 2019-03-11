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
            lst2[it] = math.trunc(lst2[it]) + 10000
    return min(lst2)






#only works for values >=0
def distexcludezero(num1, num2):
    if max([num1, num2]) > 0:
        return min(x for x in [num1, num2] if x > 0)
    else:
        return 0


def countincomp(child, father=0, mother=0):
    if father != 0:
        A = alleledist(child[0], father)
        if len(child)>1:
            C = alleledist(child[1], father)
        else:
            C = 0
    else:
        A = 0
        C = 0
    if mother != 0:
        if len(child)>1:
            B = alleledist(child[1], father)
        else:
            B = 0
        D = alleledist(child[0], mother)
    else:
        B = 0
        D = 0

    if A + B > C + D:
        return [C, D]
    elif A + B == C + D:
        if min([A,B]) < min([C,D]):
            return [A,B]
        else:
            return [C,D]
    else:
        return [A, B]