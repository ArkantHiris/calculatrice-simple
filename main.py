from features.unit_conversion import *
from features.calculatrice import * 
from features.history import *  

def interface_user() -> float:
    """
    Fonction gérant la communication de départ avec l'utilisateur
    Elle lui offre le choix entre la calculatrice et le convertisseur
    Puis apelle la fonction correspondante
    """

    print("Bonjour, que désirez vous faire : ")
    print("1. Calculatrice")
    print("2. Convertisseur")

    # Tant que l'utilisateur n'utilisera pas un des choix reconnus, il restera dans la boucle
    while True:

        # Enregistrement du choix de l'utilisateur
        choice = input("Entrez 1 ou 2 : ")      

        # Le programme ne reconnait que 1 et 2
        
        if choice == "1":

            print("Bienvenu dans la calculatrice")
            print(f"Résultat final : {calculatrice()}")

            export_history()    # On exporte l'historique des calculs
            print("Un historique de vos calculs est enregistré dans history/historique.txt")
            break

        elif choice == "2":

            menu_conversions()
            break

        else:

            print("Cette entrée n'est pas reconnue, recommencez ")



interface_user()


    
    