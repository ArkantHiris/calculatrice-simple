def subtraction(*args: float) -> float:
    """Soustrait successivement tous les arguments à partir du premier."""
    if not args:
        return 0.0
    
    resultat = args[0]
    for valeur in args[1:]:
        resultat -= valeur
    return resultat 
