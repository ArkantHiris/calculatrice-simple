import math
def logarithm(number:float, base:float=None)->float:
    """
    Prend un nombre et une base (si définie) et renvoie le
    logarithme de ce nombre.

    Args:
        number(float): Le nombre passé en paramètre
        base(int): La base du logarithme (par défaut None --> aucune)
    
    Returns:
        float: Le résultat du logarithme
    """
    try:
        if not base:
        # Si la base n'est pas définie lorsqu'on appelle la
        # fonction :
            return math.log(number)
            # On exécute le logarithme avec la base par défaut
        else:
            return math.log(number, base)
            # Sinon, on réalise l'opération avec la base passé
            # en paramètre
    except ValueError, ArithmeticError:
        # Exception si la fonction rencontre une erreur
        print("Erreur dans l'opération")

