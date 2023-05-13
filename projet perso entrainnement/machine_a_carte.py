from random import choices

def random_forme():
    print("===================================================\n")
    liste_carte = ["♠️","♣️","♦️","♥️"]
    liste_win = choices(liste_carte, k=3)

    print(liste_win)
    if liste_win[0] == liste_win[1] and liste_win[1] == liste_win[2]:
        print("===================================================\n")
        return True
    else:
        print("===================================================\n")
        return False