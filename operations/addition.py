def addition(*numbers : float) -> float:
    """
    Calcul l'addition des nombres indiqués en arguments

    [Args]:
    *numbers (float): nombres à additionner

    [Returns]:
    total (float): somme des nombres

    """

    total = 0       # Definition du total que l'on va retounrer

    # pour chaque nombre dans la liste de nombres
    for number in numbers:

        total += number     # Additionner le nombre au total

    # retourne le total
    return total
