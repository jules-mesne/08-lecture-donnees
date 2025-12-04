"""
Docstring pour main
"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as f:
        l = []
        lines = f.readlines()
        for line in lines:
            sl = []
            line = line.split(';')
            for e in line:
                sl.append(int(e))
            l.append(sl)
        return l

def get_list_k(data, k):
    """
    Docstring pour get_list_k

    Prend en argument la liste de listes retournée par read_data() 
    et un indice k et retourne la kième liste.
    
    :param data: Description
    :param k: Description
    """
    return data[k]

def get_first(l):
    """
    Docstring pour get_first

    Prend en argument une liste et retourne le premier élément de cette liste.
    
    :param l: Description
    """
    return l[0]

def get_last(l):
    """
    Docstring pour get_last

    Prend en argument une liste et retourne le dernier élément de cette liste.
    
    :param l: Description
    """
    return l[-1]

def get_max(l):
    """
    Docstring pour get_max

    Prend en argument une liste et retourne le maximum de cette liste.
    
    :param l: Description
    """
    return max(l)

def get_min(l):
    """
    Docstring pour get_min

    Prend en argument une liste et retourne le minimum de cette liste.
    
    :param l: Description
    """
    return min(l)

def get_sum(l):
    """
    Docstring pour get_sum

    Prend en argument une liste et retourne la somme de cette liste.
    
    :param l: Description
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Docstring pour main
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
    l = get_list_k(data, 37)
    print(get_first(l))
    print(get_last(l))
    print(get_max(l))
    print(get_min(l))
    print(get_sum(l))



if __name__ == "__main__":
    main()
