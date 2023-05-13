from set_up_cartes import *


def jeu_battaille():
    
    #crée le jeu de carte et le mélange
    jeu_de_carte = Cartes()
    
    jeu_de_carte.melange()
    print("===================================================\n")
    #tirage du joueur
    carte1= jeu_de_carte.tirer()
    
    print(f"tu as tirer la carte : {carte1.get_nom()}")
    
    #tirage du croupier
    carte2= jeu_de_carte.tirer()
    print(f"le croupier as tirer la carte : {carte2.get_nom()}")
    while carte1.get_force() == carte2.get_force():
        print("egalité on retire")
        carte2= jeu_de_carte.tirer()

    if carte2.get_nom() == carte1.get_nom():
        print("\n\nPAS NORMAL\n\n")
    
    #condition win 
    if carte1.get_force()>carte2.get_force():
        print("===================================================\n")
        return True
        
    else:
        print("===================================================\n")
        return False



#TEST
#for i in range(0,1000):
#jeu_battaille()