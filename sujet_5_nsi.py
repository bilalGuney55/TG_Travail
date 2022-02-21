# exo 1

def RechercheMinMax(tab : list) -> dict:
    if len(tab) == 0:
        return {'min': None, 'max': None}
    min = max = tab[0]
    for i in tab:
        if i < min:
            min = i
        elif i > max:
            max = i
    return {'min': min, 'max': max}

assert RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert RechercheMinMax([]) == {'min': None, 'max': None}


# exo 2


class Carte:

    def __init__(self, c, v):
        assert 1 <= c <= 4 and 1 <= v <= 13
        self.Couleur = c
        self.Valeur = v

    
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    
    def __init__(self):
        self.contenu = []

    
    def remplir(self):
        for couleur in range(1,5):
            for nom in range(1, 14):
                self.contenu.append(Carte(couleur, nom))

    
    def getCarteAt(self, pos):
        assert 0 < pos < 4 * 13
        return self.contenu[pos-1]

unPaquet = PaquetDeCarte()
unPaquet.remplir()

uneCarte = unPaquet.getCarteAt(1)
assert uneCarte.getNom() == "As"
assert uneCarte.getCouleur() == "pique"

uneCarte = unPaquet.getCarteAt(2)
assert uneCarte.getNom() == '2'
assert uneCarte.getCouleur() == "pique"

uneCarte = unPaquet.getCarteAt(14)
assert uneCarte.getNom() == "As"
assert uneCarte.getCouleur() == "coeur"

uneCarte = unPaquet.getCarteAt(20)
assert uneCarte.getNom() == '7'
assert uneCarte.getCouleur() == "coeur"

uneCarte = unPaquet.getCarteAt(27)
assert uneCarte.getNom() == "As"
assert uneCarte.getCouleur() == "carreau"