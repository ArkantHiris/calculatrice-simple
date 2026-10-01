# Fichier principal contenant toutes les fonctions

from operations.addition import addition
from operations.multiply import multiply
from operations.subtraction import subtraction
from operations.division import division


def user_interaction():

    valid_choices = ["+","-","*","/","="]
    current_requirement = "number"
    first_entry = True

    operator = ""
    total = None
    number = None

    while operator != "=":

        if current_requirement == "number":

            while True:

                entry =  input("Entrez un nombre : ").strip()
                entry = entry.replace(",",".")

                try:
                    value = float(entry)
                    if first_entry == True:

                        total = value
                        first_entry = False

                    else:

                        number = value

                    current_requirement = "operator"
                    break

                except ValueError:
                    print("Erreur : veuillez entrez un nombre entier ou décimal ")

        else:

            while True:

                entry = input("Entrez un opérateur : ").strip()

                if entry in valid_choices:

                    operator = entry
                    current_requirement = "number"
                    break

                else:
                    print("Cet opérateur n'est pas reconnu ")

        if total and operator and number:


            if operator == "+":
            
                total = addition(total, number)
                number = None
            
            
            elif operator == "-":
            
                total = subtraction(total, number)
                number = None
            
            
            elif operator == "*":
            
                total = multiply(total, number)
                number = None

            elif operator == "/":

                total = division(total, number)
                number = None

            print(total)


    return total
    

print(user_interaction())



    
    