import math

def sine(angle:float)->float:
    """
    Renvoie le sinus d'un angle

    Args:
        angle(float): Les degrés passé en argument
    Returns:
        float: Le résultat de l'opération
    Raises:
        (ArithmeticError, ValueError): si la fonction rencontre une erreur, lève une fonction
    """
    try:
        return math.sin(math.radians(angle))
        # Conversion des degrés de l'angle en radians avec
        # math.radians()
    except ArithmeticError, ValueError:
        print("Erreur dans l'opération")


def consine(angle:float)->float:
    """
    Renvoie le cosinus d'un angle

    Args:
        angle(float): Les degrés passé en argument
    Returns:
        float: Le résultat de l'opération
    Raises:
        (ArithmeticError, ValueError): Si la fonction rencontre une erreur, lève une fonction
    """
    try:
        return math.cos(math.radians(angle))
        # Conversion des degrés de l'angle en radians avec
        # math.radians()
    except ArithmeticError, ValueError:
        print("Erreur dans l'opération")


def tangent(angle:float)->float:
    """
    Renvoie le cosinus d'un angle
    Args:
        angle(float): Les degrés passé en argument
    Returns:
        float: Le résultat de l'opération
    Raises:
        (ArithmeticError, ValueError): Si la fonction rencontre une erreur, lève une fonction
    """
    try:
        return math.tan(math.radians(angle))
        # Conversion des degrés de l'angle en radians avec
        # math.radians()
    except ArithmeticError, ValueError:
        print("Erreur dans l'opération")
