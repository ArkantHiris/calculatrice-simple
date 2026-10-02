from unit_conversion import *
from calculatrice import *   

def interface_user() -> float:
    """
    Fonction gérant la communication de départ avec l'utilisateur
    Elle lui offre le choix entre la calculatrice et le convertisseur
    Puis apelle la fonction correspondante
    """

    print("Bonjour, que désirez vous faire : ")
    print("1. Calculatrice")
    print("2. Convertisseur")

    # Enregistrement du choix de l'utilisateur
    choice = input("Entrez 1 ou 2 : ")

    # Tant que l'utilisateur n'utilisera pas un des choix reconnus, il restera dans la boucle
    while True:

        # Le programme ne reconnait que 1 et 2
        try:
            if choice == "1":

                print(calculatrice())
                break

            elif choice == "2":

                menu_conversions()
                break

        except ValueError:

            print("Cette entrée n'est pas reconnue, recommencez ")


interface_user()


    
    