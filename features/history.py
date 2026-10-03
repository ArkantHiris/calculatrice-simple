calcul_history = []

def update_history(operator : str, total : float, number1 : float, number2 : float) -> None:
    """
    Fonction permettant de mettre à jour l'historique des calculs

    [Args]
    operator (str): l'opérateur utilisé pour ce calcul
    total (float): le total du calcul déjà réalisé par la fonction calculatrice
    number1 (float): le premier nombre, toujours nécessaire pour le calcul
    number2 (float): le second nombre, nécessaire uniquement pour les calculs à deux nombres
    """

    # Liste des deux types d'operateurs, l'un demandant deux entrée, et l'autre qu'un seul
    two_values_operators = ["+", "-", "*", "/", "%", "**"]
    one_value_operators = ["root","racine","cos","sin","tan","log"]

    # Si l'opérateur est de la première catégorie
    if operator in two_values_operators:

        # Alors on enregistre le calcul sous ce format
        calcul_history.append(f"{number1} {operator} {number2} = {total}")

    # Si l'opérateur est de la seconde catégorie
    elif operator in one_value_operators:

        # Alors on enregistre le calcul sous cet autre format
        calcul_history.append(f"{operator} {number1} = {total}")


def export_history() -> None:
    """
    Fonction exportant la variable globale calcul_history sous forme d'un fichier texte :
    Un calcul par ligne
    """

    # On ouvre le fichier historique, w indique qu'on efface l'ancien contenu pour le remplacer
    with open("history/historique.txt", "w", encoding="utf-8") as f:

        # Pour chaque calcul
        for calcul in calcul_history:

            # On écrit une ligne
            f.write(f"{calcul}\n")