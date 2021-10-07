
## exercice 1


def somme_recursif(n):
    if n == 0 :
        return 0
    else : 
        return n + somme_recursif(n-1)

somme_recursif(4)

def somme_iteratif(n):
    res = 0
    v = 0
    while v <= n :
        res = res + v
        v = v + 1
    return res

somme_iteratif(4)





def somme_iteratif2(n):
    res = 0
    for v in range(n+1):
        res = res + v
    return res

somme_iteratif2(4)



##### exercice 2



def prems(n):
    if 

