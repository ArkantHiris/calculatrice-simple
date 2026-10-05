from operations.addition import addition
from operations.multiply import multiply
from operations.subtraction import subtraction
from operations.division import division
from operations.modulo import modulo
from operations.exponentiation import exponentiation
from operations.square_root import square_root
from operations.trigonometry import sine, consine, tangent
from operations.logarithm import logarithm
from features.history import update_history

def calculatrice() -> float:
    """
    Fonction récupérant les inputs de l'utilisateur telle une calculatrice
    On demande un premier nombre ( qui sera contrôlé ), puis un opérateur ( contrôlé aussi ) et enfin un second nombre.
    L'entrée du second nombre lance le calcul du premier total.
    L'utilisateur a ensuite la possibilité de cloturer le calcul avec "=" et obtenir le résultat ou continuer en entrant un
    nouvel opérateur.

    Cas particulier de l'opérateur qui n'a besoin que d'une seule valeur. Le calcul est déclenché dès l'entrée de l'opérateur.

    Après chaque calcul, on apelle la fonction update_history pour mettre à jour l'historique.

    [Returns]:
    total (float): Le résultat des calculs
    """

    # Liste des opérateurs reconnus par le programme, dans le cas de deux valeurs nécessaires.
    two_values_operators = ["+", "-", "*", "/", "%", "**", "="]

    # Liste des opérateurs reconnus par le programme, dans le cas d'une seule valeur nécessaire.
    one_value_operators = ["root","racine","cos","sin","tan","log"]

    # Statut du calcul (number ou operator) indiquant à quelle étape du calcul nous sommes   
    current_requirement = "number"

    # Statut du calcul (True ou False) indiquant si nous sommes à la première entrée ou non
    first_entry = True

    # L'opérateur entré en dernier
    operator = ""

    # Le résultat du calcul
    total = None

    # Le dernier nombre entré par l'utilisateur
    number = None

    # Tant que l'utilisateur n'entre pas l'opérateur "=", on continue le calcul
    while operator != "=":

        # Si un nombre est demandé
        if current_requirement == "number":

            # Tant que l'utilisateur ne nous a pas envoyé un nombre correct, on reste dans la boucle
            while True:

                # Récupère l'entrée de l'utilisateur et retire les caractères spéciaux
                entry =  input("Entrez un nombre : ").strip()
                # Pour les français, on remplace les virgules par des points
                entry = entry.replace(",",".")

                # On essaye d'attribuer cette entrée à nos variables, à la moindre erreur, on part en exception
                try:

                    # On transforme en float l'entrée de l'utilisateur (qui était en str)
                    value = float(entry)

                    # Si c'est la première entrée de l'utilisateur
                    if first_entry == True:

                        # Alors total est égal à value
                        total = value
                        # Et on retire le statut de première entrée, car total ne sera plus nul
                        first_entry = False

                    # Sinon, c'est number qui est égal à value
                    else:

                        number = value

                    # On a maintenant besoin d'un opérateur
                    current_requirement = "operator"
                    # On sort de la boucle
                    break

                # Si une erreur est survenue, on retourne dans la boucle
                except ValueError:
                    print("Erreur : veuillez entrez un nombre entier ou décimal ")

        # Sinon on demande un opérateur
        else:

            # Tant que l'utilisateur ne nous a pas envoyé un opérateur correct, on reste dans la boucle
            while True:

                # Récupère l'entrée de l'utilisateur et retire les caractères spéciaux
                entry = input("Entrez un opérateur : ").strip()
                entry = entry.lower()

                # Si l'opérateur fait bien parti des opérateurs autorisés pour deux valeurs
                if entry in two_values_operators:

                    # On applique entry à operator
                    operator = entry
                    # On a maintenant besoin d'un nombre
                    current_requirement = "number"
                    # On sort de la boucle
                    break

                # Si l'opérateur fait bien parti des opérateurs autorisés pour une valeur
                elif entry in one_value_operators:

                    # Selon l'opérateur choisi, on entre dans une condition différente
                    # Et on apelle la fonction correspondante
                    # Puis on met à jour total

                    history_total = total

                    if entry == "root" or entry == "racine":

                        total = square_root(total)
                        update_history(entry, total, history_total, 0)

                    elif entry == "sin":

                        total = sine(total)
                        update_history(entry, total, history_total, 0)

                    elif entry == "cos":

                        total = consine(total)
                        update_history(entry, total, history_total, 0)

                    elif entry == "tan":

                        total = tangent(total)
                        update_history(entry, total, history_total, 0)

                    elif entry == "log":

                        total = logarithm(total)
                        update_history(entry, total, history_total, 0)

                    print(f"Résultat : {total}")
                
                # Sinon on explique que le choix n'est pas valide et on retourne dans la boucle
                else:
                    print("Cet opérateur n'est pas reconnu ")

        # Si total et number sont différents de None, et qu'opérateur n'est pas vide
        if total != None and operator != "" and number != None:

            # Selon l'opérateur choisi, on entre dans une condition differente
            # On apelle la fonction correspondante pour mettre à jour total
            # Et number repasse en None

            history_total = total

            if operator == "+":

                total = addition(total, number)
                update_history(operator, total, history_total, number)
                number = None
            
            
            elif operator == "-":

                total = subtraction(total, number)
                update_history(operator, total, history_total, number)
                number = None
                
            elif operator == "*":

                total = multiply(total, number)
                update_history(operator, total, history_total, number)
                number = None

            elif operator == "/":

                total = division(total, number)
                update_history(operator, total, history_total, number)
                number = None

            elif operator == "%":

                total = modulo(total, number)
                update_history(operator, total, history_total, number)
                number = None

            elif operator == "**":

                total = exponentiation(total, number)
                update_history(operator, total, history_total, number)
                number = None

            print(f"Résultat : {total}")


    # On retourne le total si "=" est entré
    return total