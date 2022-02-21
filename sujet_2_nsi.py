# exo 1

def moyenne(liste : list) -> float:
    somme = 0
    total = 0
    for (note, coefficient) in liste:
        somme += note * coefficient
        total += coefficient
    if total != 0:
        return somme / total
    return 0

assert moyenne([]) == 0
assert moyenne([(1, 0)]) == 0
assert moyenne([(1, 1)]) == 1
assert moyenne([(15,2), (9,1), (12,3)]) == 12.5


# exo 2


def pascal(n : int) -> list:
    C= [[1]]
    for k in range(1, n+1):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

assert pascal(0) == [[1]]
assert pascal(1) == [[1], [1, 1]]
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]