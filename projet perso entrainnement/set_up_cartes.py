import random

class Carte:
    def __init__(self, val, forme , force):
        self.valeur = val
        self.forme = forme
        self.force = force

    def get_force(self):
        return self.force
    
    def get_nom(self):
        return self.valeur+" DE "+self.forme

class Cartes: 
    def __init__(self):
        valeurs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "VALET", "DAME", "ROI", "AS"]
        formes = ["CARREAU", "COEUR", "PIQUE", "TREFLE"]
        self.cartes=[]
        for forme in formes:
            for i, val in enumerate(valeurs):
                force= i+1
                self.cartes.append(Carte(val, forme, force))
    
    def melange(self):
        random.shuffle(self.cartes)

    def afficher(self):
        for card in self.cartes:
            print(card.get_nom())
    

    def tirer(self):
        x= random.randint(0, len(self.cartes)-1)
        v=self.cartes[x]
        del self.cartes[x]
        return v






