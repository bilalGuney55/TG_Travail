class Pile:
    def __init__(self): # Les éléments sont stockés dans une liste python
        self.data = []
      
    def est_vide(self):
        return len(self.data) == 0 
    
    # Le choix suivant a été fait : Le sommet de la pile correspond au dernier élément de la liste
    
    def empile(self,x):
        self.data.insert(0,x)

    def depile(self):
        assert not self.est_vide(), "Vous avez essayé de dépiler une pile vide !"
        for e in self.data:
            self.data = self.data - self.data[0]
        return self.data
            

    def __repr__(self):       # Hors-Programme : pour afficher convenablement la pile
        s = "".center(5, "-") + "\n"              
        for i in range(len(self.data)-1, -1, -1) :
            s = s + str(self.data[i]).center(5) + "\n" + "".center(5, "-") + "\n"
        return s
    
    

p = Pile() # Création de l'objet 
p.empile(5)
p.empile(3)
p.empile(7)

print(p)
