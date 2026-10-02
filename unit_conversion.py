# Constante physique (température la plus basse théoriquement atteignable)
ZERO_ABSOLU_CELSIUS = -273.15
ZERO_ABSOLU_FAHRENHEIT = -459.67
ZERO_ABSOLU_KELVIN = 0.0


def km_to_miles(km: float) -> float:
    return round(km * 0.621371, 2)


def miles_to_km(miles: float) -> float:
    return round(miles / 0.621371, 2)


def kg_to_livres(kg: float) -> float:
    return round(kg * 2.20462, 2)


def livres_to_kg(livres: float) -> float:
    return round(livres / 2.20462, 2)

def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < ZERO_ABSOLU_CELSIUS:
        raise ValueError(f"La température ne peut pas être inférieure au zéro absolu: ({ZERO_ABSOLU_CELSIUS} °C).")
    return round((celsius * 9 / 5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    if fahrenheit < ZERO_ABSOLU_FAHRENHEIT:
        raise ValueError(f"La température ne peut pas être inférieure au zéro absolu: ({ZERO_ABSOLU_FAHRENHEIT} °F).")
    return round((fahrenheit - 32) * 5 / 9, 2)


def celsius_to_kelvin(celsius: float) -> float:
    if celsius < ZERO_ABSOLU_CELSIUS:
        raise ValueError(f"La température ne peut pas être inférieure au zéro absolu: ({ZERO_ABSOLU_CELSIUS} °C).")
    return round(celsius + 273.15, 2)


def kelvin_to_celsius(kelvin: float) -> float:
    if kelvin < ZERO_ABSOLU_KELVIN:
        raise ValueError(f"La température en Kelvin ne peut pas être négative.")
    return round(kelvin - 273.15, 2)


def menu_conversions():
    """Menu interactif de conversion d'unités."""
    while True:
        print("\n--- CONVERSION D'UNITÉS ---")
        print("1. Kilomètres -> Miles")
        print("2. Miles -> Kilomètres")
        print("3. Kilogrammes -> Livres")
        print("4. Livres -> Kilogrammes")
        print("5. Celsius -> Fahrenheit")
        print("6. Fahrenheit -> Celsius")
        print("7. Celsius -> Kelvin")
        print("8. Kelvin -> Celsius")
        print("9. Quitter l'application")

        choix = input("\nChoisissez une option (1-9) : ")

        try:
            if choix == "1":
                val = input("Entrez la distance en km : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} km = {km_to_miles(val)} miles")

            elif choix == "2":
                val = input("Entrez la distance en miles : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} miles = {miles_to_km(val)} km")

            elif choix == "3":
                val = input("Entrez le poids en kg : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} kg = {kg_to_livres(val)} lbs")

            elif choix == "4":
                val =input("Entrez le poids en lbs : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} lbs = {livres_to_kg(val)} kg")

            elif choix == "5":
                val = input("Entrez la température en °Celsius : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} °C = {celsius_to_fahrenheit(val)} °F")

            elif choix == "6":
                val = input("Entrez la température en °Fahrenheit : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} °F = {fahrenheit_to_celsius(val)} °C")

            elif choix == "7":
                val = input("Entrez la température en °Celsius : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} °C = {celsius_to_kelvin(val)} K")

            elif choix == "8":
                val = input("Entrez la température en Kelvin : ")
                val = float(val.replace(",", "."))
                print(f"Résultat : {val} K = {kelvin_to_celsius(val)} °C")

            elif choix == "9":
                print("\nAu revoir!")
                return
            else:
                print("Option invalide.")
        except ValueError as err:
            print(f"Erreur : {err}")

