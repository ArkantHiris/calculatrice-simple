import math
def square_root(number:float)-> float:
    """
    Prend en tant qu'argument un nombre (entier ou à virgules) et renvoie la racine carrée de ce nombre.

    Args:
        number(float): Le nombre passé dans les arguments.
    Returns:
        float: Le résultat de l'opération.
    Raises:
        ValueError: Si un nombre négatif est passé en tant qu'argument, lève une exception.
    """
    try:
        # Utilisation de la fonction sqrt de math pour
        # calculer la racine carrée
        return math.sqrt(number)
    except ValueError:
        # Lève une exception si number est négatif
        print("Erreur dans l'opération")