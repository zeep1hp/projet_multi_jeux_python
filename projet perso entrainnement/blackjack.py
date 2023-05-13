from set_up_cartes import *


    
    
    
def jeu_blacjack():
    jeu_carte = Cartes()
    jeu_carte.melange()
    print("===================================================\n")
    print("TOUR DU JOUEUR")
    carte1 = jeu_carte.tirer()
    print(carte1.get_nom())
    carte2 = jeu_carte.tirer()
    print(carte2.get_nom())
    main_joueur =carte1.get_force()+ carte2.get_force()
    print(f"la valeur des cartes du joueur est de : {main_joueur}\n")
    x = input("veut tu retirer une carte ? (oui|pour retirer)\n==>")
    if x == "oui" or x=="OUI":
        carte_bonus = jeu_carte.tirer()
        main_joueur += carte_bonus.get_force()
        print(f"la valeur de ta main est de : {main_joueur}\n")
    if main_joueur > 21:
        print("TU A DEPASSER 21")
        print("===================================================\n")
        return False
    print("TOUR DU CROUPIER")
    carte_c1 = jeu_carte.tirer()
    print(carte_c1.get_nom())
    carte_c2 = jeu_carte.tirer()
    print(carte_c2.get_nom())
    main_croupier = carte_c1.get_force()+ carte_c2.get_force()
    while main_croupier <= 15:
        print("le croupier retire une carte")
        carte_bonus = jeu_carte.tirer()
        print(carte_bonus.get_force())
        main_croupier += carte_bonus.get_force()
    print(f"la valeur des cartes du croupier est de : {main_croupier}\n")
    if main_croupier > 21:
        print("LE CROUPIER A DEPASSER 21")
        print("===================================================\n")
        return True

    
    if main_joueur > main_croupier:
        return True
    elif main_joueur == main_croupier:
        print("EGALITER")
    else:
        print("===================================================\n")
        return False
    

#TEST
#for i in range(0,10):
#x = jeu_blacjack()
#print(f"j'ai gagner ! c'est {x}!")