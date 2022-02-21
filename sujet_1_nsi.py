## exerice 1

def recherche(caractere : str, mot : str) -> int:
    """ le nombre de fois où caractere apparaît dans mot. """
    total = 0
    for m in mot:
        if m == caractere:
            total += 1
    return total

assert recherche('e', "sciences") == 2
assert recherche('i',"mississippi") == 4
assert recherche('a',"mississippi") == 0



## exercice 2

Pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre : int, solution : list =[], i : int =0) -> list:
    if arendre == 0:
       return solution
    p = Pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

assert rendu_glouton(68,  [], 0) == [50, 10, 5, 2, 1]
assert rendu_glouton(291, [], 0) == [100, 100, 50, 20, 20, 1]
