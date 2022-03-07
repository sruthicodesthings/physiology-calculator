import math


def bmi(weight_kg: float, height_m: float) -> float:
    """Calculates BMI from weight and height."""
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height have to be more than 0.")
    return weight_kg / (height_m ** 2)


def bsa_mosteller(weight_kg: float, height_cm: float) -> float:
    """Calculates BSA using the Mosteller formula."""
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height have to be more than 0.")
    return math.sqrt((height_cm * weight_kg) / 3600)


def bsa_dubois(weight_kg: float, height_cm: float) -> float:
    """Another BSA calculation, this time using the Du Bois formula."""
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height have to be more than 0.")
    return 0.007184 * (height_cm ** 0.725) * (weight_kg ** 0.425)
