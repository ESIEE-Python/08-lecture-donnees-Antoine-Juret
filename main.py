""" ce fichier permet de retourner une liste csv 
et d'appeler différente foncton
"""
#### Imports et définition des variables globales

import csv




#### Fonctions secondaires

def read_data(filename:str):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as file:
        reader=csv.reader(file,delimiter=";")
        return [list(map(int,ligne))for ligne in reader]

def get_list_k(l, k):
    """Retourne la k-ième liste de la liste retourné par readdata

    Args:
       l: Liste de listes d'entiers.
        k (int): L'indice de la liste à retourner.

    Returns:
        list: La k-ième liste ou None si l'indice est invalide.
    """
    if 0 <= k < len(l):
        return l[k]
    print(f"Indice k={k} est hors limites. La longueur de data est {len(l)}.")
    return None





def get_last(l):
    """ retourne le dernier élément de la liste
    """
    if l :
        return l[-1]
    return None

def get_first(l):
    """ retourne le premier éléments de la liste
    Arg l = liste 
    """
    return l[0] if l else None




def get_max(l):
    """Retourne le maximum de la liste.

    Args:
        l (list): Une liste d'entiers.

    Returns:
        int: Le maximum de la liste.
    """
    return max(l) if l else None




def get_min(l):
    """Retourne le minimum de la liste.

    Args:
        l (list): Une liste d'entiers.

    Returns:
        int: Le minimum de la liste.
    """
    return min(l) if l else None




def get_sum(l):
    """Retourne la somme de la liste.

    Args:
        l (list): Une liste d'entiers.

    Returns:
        int: La somme de la liste.
    """

    return sum(l) if l else None



#### Fonction principale


def main():
    """ appel de la fonction """
    filename = 'listes.csv'  # data = read_data(FILENAME)
    l = read_data(filename)

    print("Données lues :", l)

    k=37
    print(k,get_list_k(l,k))

    first_list = get_list_k(l, 0)

    print("Premier élément de la première liste :", get_first(first_list))
    print("Dernier élément de la première liste :", get_last(first_list))
    print("Maximum de la première liste :", get_max(first_list))
    print("Minimum de la première liste :", get_min(first_list))
    print("Somme de la première liste :", get_sum(first_list))


    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
