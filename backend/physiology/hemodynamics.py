def mean_arterial_pressure(systolic_bp: float, diastolic_bp: float) -> float:
    """Estimates mean arterial pressure (MAP)."""
    if systolic_bp <= 0 or diastolic_bp <= 0:
        raise ValueError("Blood pressure has to be more than 0.")
    if systolic_bp < diastolic_bp:
        raise ValueError("Systolic BP should be higher than diastolic BP.")
    return (systolic_bp + 2 * diastolic_bp) / 3


def pulse_pressure(systolic_bp: float, diastolic_bp: float) -> float:
    """Pulse pressure is just systolic BP minus diastolic BP."""
    if systolic_bp <= 0 or diastolic_bp <= 0:
        raise ValueError("Blood pressure has to be more than 0.")
    if systolic_bp < diastolic_bp:
        raise ValueError("Systolic BP should be higher than diastolic BP.")
    return systolic_bp - diastolic_bp


def cardiac_output(heart_rate_bpm: float, stroke_volume_ml: float) -> float:
    """Works out how many liters of blood the heart pumps each minute."""
    if heart_rate_bpm <= 0 or stroke_volume_ml <= 0:
        raise ValueError("Heart rate and stroke volume have to be more than 0.")
    return heart_rate_bpm * stroke_volume_ml / 1000


def cardiac_index(cardiac_output_l_min: float, bsa_m2: float) -> float:
    """Cardiac output adjusted for body surface area."""
    if cardiac_output_l_min <= 0 or bsa_m2 <= 0:
        raise ValueError("Cardiac output and BSA have to be more than 0.")
    return cardiac_output_l_min / bsa_m2


def systemic_vascular_resistance(map_mmhg: float, cvp_mmhg: float, cardiac_output_l_min: float) -> float:
    """Estimates SVR. The x80 part changes it into the usual units."""
    if cardiac_output_l_min <= 0:
        raise ValueError("Cardiac output has to be more than 0.")
    if map_mmhg < 0 or cvp_mmhg < 0:
        raise ValueError("Pressures can't be negative here.")
    return 80 * (map_mmhg - cvp_mmhg) / cardiac_output_l_min
