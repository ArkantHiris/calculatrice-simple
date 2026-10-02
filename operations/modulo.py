def modulo(*numbers:float)->float:
    """
    Prends en paramètre des nombres (entier ou à virgule) et
    renvoie le reste de la division.

    Args:
        numbers (float): Les nombres passés en paramètre

    Returns:
        float: Le résultat de l'opération

    Raises:
        ArithmeticError: Lève une erreur si on tente de faire modulo avec 0
    """
    try:
        total = numbers[0]
        # On prend le premier chiffre au début de la
        # fonction
        for i in range(len(numbers)-1):
        # Pour chaque autre nombre passé en paramètre
            total%=numbers[i+1]
            # On affecte le total par l'opération modulo
            # avec le chiffre d'après
        return total
    except ArithmeticError:
        # ArithmeticError --> classe qui lève les exceptions
        # dans les calculs arithmétiques (ex : division par 0)
        # On lève une exception si la fonction rencontre une
        # erreur
        print("Erreur dans l'opération")

# En ce qui concerne les chiffre négatifs, le modulo % s'assure
# que le signe du résultat (positif ou négatif) correspond à
# celui du diviseur
# Explications : https://www.geeksforgeeks.org/python/how-to-perform-modulo-with-negative-values-in-python/