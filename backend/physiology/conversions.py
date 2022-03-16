def kg_to_lb(kg: float) -> float:
    """Kilograms to pounds."""
    return kg * 2.2046226218


def lb_to_kg(lb: float) -> float:
    """Pounds to kilograms."""
    return lb / 2.2046226218


def cm_to_inches(cm: float) -> float:
    """Centimeters to inches."""
    return cm / 2.54


def inches_to_cm(inches: float) -> float:
    """Inches to centimeters."""
    return inches * 2.54


def celsius_to_fahrenheit(celsius: float) -> float:
    """Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9
