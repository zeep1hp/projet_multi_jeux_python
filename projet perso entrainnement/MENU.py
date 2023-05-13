from set_up_cartes import *
from BATAILLE import jeu_battaille
from blackjack  import jeu_blacjack
from machine_a_carte import random_forme
from memo_carte import memo

def lecture():

    with open("porte_monnaie.txt", "r") as file:
        x = file.readlines()
        for i in x:
            i= x[0]
        file.close()
        return i 

def sauvegarde():
    global porte_monnaie
    with open("porte_monnaie.txt", "w") as file:
        file.write(str(porte_monnaie))
        file.close()


def menu_principal():
    global porte_monnaie
    g = True
    while g: 
        liste_choix = ["1","2","3","4","quit"]
        menu = {
            '1' : jeu_blacjack,
            '2' : jeu_battaille,
            '3' : random_forme,
            '4':memo
        }
        print("===================================================\n")
        print("***************")
        print("*             *")
        print("*    MENU     *")
        print("*  PRINCIPAL  *")
        print("*             *")
        print("***************")
        print(f"\ntu a actuellemnt {porte_monnaie}")
        choix = input("\n[1] Blackjack\n[2] Bataille\n[3] MACHINE A CARTE\n[4] TOUVER LA BONNE CARTE\n\n[quit] QUITTEZ\n==>")
        while choix not in liste_choix:
            choix = input("\n[1] Blackjack\n[2] Bataille\n[3] MACHINE A CARTE\n[4] TOUVER LA BONNE CARTE\n\n[quit] QUITTEZ\n==>")
        if choix == "quit":
            g=False
            break
        mise = input("Combien souhaite tu miser ?\n==>")
        verif = mise.isdigit()
        while verif is not True:
            print("entre un nombre valide")
            mise = input("Combien souhaite tu miser ?\n==>")
            verif = mise.isdigit()
        mise = int(mise)
        porte_monnaie-=mise
        sauvegarde()
        for cle, valeur in menu.items():
            if choix == cle:
                jeu = valeur()
                if jeu is True:
                    
                    porte_monnaie+=(mise*2)
                    sauvegarde()
                    print(f"TU A GAGNER + {mise}")
                    print("===================================================\n")
                else:
                    
                    print("TU A PERDU")
                    print("===================================================\n")
        


porte_monnaie =int(lecture())
menu_principal()