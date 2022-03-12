def minute_ventilation(respiratory_rate: float, tidal_volume_ml: float) -> float:
    """How much air moves in and out of the lungs each minute, in L/min."""
    if respiratory_rate <= 0 or tidal_volume_ml <= 0:
        raise ValueError("Respiratory rate and tidal volume have to be more than 0.")
    return respiratory_rate * tidal_volume_ml / 1000


def alveolar_ventilation(respiratory_rate: float, tidal_volume_ml: float, dead_space_ml: float) -> float:
    """Like minute ventilation, except it removes the dead-space air."""
    if respiratory_rate <= 0 or tidal_volume_ml <= 0:
        raise ValueError("Respiratory rate and tidal volume have to be more than 0.")
    if dead_space_ml < 0 or dead_space_ml >= tidal_volume_ml:
        raise ValueError("Dead space has to be between 0 and tidal volume.")
    return respiratory_rate * (tidal_volume_ml - dead_space_ml) / 1000


def pf_ratio(pao2_mmhg: float, fio2: float) -> float:
    """Calculates the P/F ratio from PaO2 and FiO2 written as a decimal."""
    if pao2_mmhg <= 0 or fio2 <= 0 or fio2 > 1:
        raise ValueError("PaO2 has to be positive and FiO2 has to be between 0 and 1.")
    return pao2_mmhg / fio2
