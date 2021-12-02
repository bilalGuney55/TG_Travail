#CODE PILE

def creer_pile():
    """ Créé une pile vide
    :return: Une pile vide représentée par la liste vide
    """
    return []


def est_vide(p):
    """ Teste si une pile est vide
    :param p: Une pile
    :return: True si p est vide, False sinon
    """
    return p == []


def empiler(p, e):
    """ Empile un élément au sommet d'une pile
    :param p: Une pile
    :param e: Un élément
    :return: None
    :Effets: Empile e au sommet de p
    """
    p.append(e)
    

def depiler(p):
    """ Dépile un élément au sommet d'une pile et le renvoie
    :param p: Une pile
    :return: L'élément au sommet de la pile
    :Précondition: p est non vide
    """
    assert not est_vide(p), "Impossible de dépiler une pile vide"
    return p.pop()



#exercice_1


def pile_alterne(n):
    p = creer_pile()
    for i in range(n):
        if (i % 2) == 0:
            empiler(p,i)
        else:
            empiler(p,-i)
    return p    
    


# exercice_2


def vider_pile(p):
    while est_vide(p) == False:
        depiler(p)
                   
               
        
def sommet_pile(p):
    if est_vide == True:
        return None
    else:
        res = depiler(p)
        empiler(p,res)
        return res
    
        
# ex_3

def est_bien_parenthesee(parent):
    p = creer_pile()
    for i in parent:
        if parent == "(":
            empiler(p,"(")
        elif parent == ")":
            if est_vide(p) == False:
                depiler(p)
            else:
                return False
    return est_vide(p)





##exercice_4


def separer_expression(liste):
    liste = []
    for e in liste:
        liste.split(" ")
    return liste
    
print(separer_expression("3 5 + 4 2 - *"))



## exercice 6


class Pile:
    
    def __init__(self,taille_max):
        self.taille_max = taille_max
        self.taille = 0
        self.contenu = []
        for i in range(taille_max):
            self.contenu = self.contenu + [None]
            
    
    def est_vide(self):
        if self.taille_max == 0:
            return True
        
        
