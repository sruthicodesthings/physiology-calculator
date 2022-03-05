import math


def bmi(weight_kg, height_m):
    # bmi is weight divided by height squared
    return weight_kg / (height_m ** 2)


def bsa_mosteller(weight_kg, height_cm):
    # body surface area using the Mosteller formula
    return math.sqrt((height_cm * weight_kg) / 3600)


def bsa_dubois(weight_kg, height_cm):
    # found another formula for BSA so adding it too
    return 0.007184 * (height_cm ** 0.725) * (weight_kg ** 0.425)
