import random
import numpy as np

def memo():
    list_map = []
    map1 = [["🃏","🎴","🎴"],["🎴","🎴","🎴"],["🎴","🎴","🎴"]]
    list_map.append(map1)
    map2 = [["🎴","🃏","🎴"],["🎴","🎴","🎴"],["🎴","🎴","🎴"]]
    list_map.append(map2)
    map3 = [["🎴","🎴","🃏"],["🎴","🎴","🎴"],["🎴","🎴","🎴"]]
    list_map.append(map3)
    map4 = [["🎴","🎴","🎴"],["🃏","🎴","🎴"],["🎴","🎴","🎴"]]
    list_map.append(map4)
    map5 = [["🎴","🎴","🎴"],["🎴","🃏","🎴"],["🎴","🎴","🎴"]]
    list_map.append(map5)
    map6 = [["🎴","🎴","🎴"],["🎴","🎴","🃏"],["🎴","🎴","🎴"]]
    list_map.append(map6)
    map7 = [["🎴","🎴","🎴"],["🎴","🎴","🎴"],["🃏","🎴","🎴"]]
    list_map.append(map7)
    map8 = [["🎴","🎴","🎴"],["🎴","🎴","🎴"],["🎴","🃏","🎴"]]
    list_map.append(map8)
    map9 = [["🎴","🎴","🎴"],["🎴","🎴","🎴"],["🎴","🎴","🃏"]]
    list_map.append(map9)
    map_cacher = np.array([["🎴","🎴","🎴"],["🎴","🎴","🎴"],["🎴","🎴","🎴"]])
       

    map_choix =np.array([["1","2","3"],["4","5","6"],["7","8","9"]])
    

    dico_map ={
        '1':np.array(map1),
        '2':np.array(map2),
        '3':np.array(map3),
        '4':np.array(map4),
        '5':np.array(map5),
        '6':np.array(map6),
        '7':np.array(map7),
        '8':np.array(map8),
        '9':np.array(map9)
    }
    
    choix_aleatoire = random.choice(list_map)
    choix_aleatoire = np.array(choix_aleatoire)
    
    vie = 3
    
    print("En suivant cette notation:")
    print(map_choix)
    print("Trouvez la case ou se cache 🃏")
    
    while vie >=0:
        print("===================================================\n")
        print(map_cacher)
        print(f"tu a {vie} vie")
        choix = input("quel case veut tu jouer :\n==>")
        for cle, maps in dico_map.items():
            if choix == cle:
                if np.array_equal(maps, choix_aleatoire):
                    print(f"BONNE REPONSE :\n{choix_aleatoire}")
                    print("===================================================\n")
                    return True
                    
                else:
                    vie-=1
                    print("perdu")
                    print("===================================================\n")    

    else:
        print(f"voicie la reponse :\n{choix_aleatoire}")
        print("===================================================\n")
        return False





