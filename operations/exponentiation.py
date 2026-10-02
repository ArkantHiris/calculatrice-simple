def exponentiation(*numbers: float) -> float:
    """
    Prends en paramètre des nombres (entier ou à virgule). Le premier
    est la base et les suivants les exposants, et renvoie le résultat.

    Args:
        numbers (float): Les nombres passés en paramètre

    Returns:
        float: Le résultat de l'opération
    """
    if not numbers:
        return 0.0

    #On prend le premier nombre donné en argument comme base
    resultat = numbers[0]

    #Pour chaque autre nombre en argument
    for valeur in numbers[1:]:
        resultat **= valeur
    return resultat