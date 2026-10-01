def division(*args: float) -> float:
    """ Divise la première valeur par toutes les autres dans l'ordre."""
    if not args:
        return 0.0
    
    resultat = args[0]
    for valeur in args[1:]:
        if valeur == 0:
            return ValueError("Division par zéro impossible.")
        resultat /= valeur
    return resultat
