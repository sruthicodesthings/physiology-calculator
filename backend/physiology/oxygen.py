def arterial_oxygen_content(hemoglobin_g_dl: float, sao2: float, pao2_mmhg: float) -> float:
    """Estimates how much oxygen is in arterial blood (mL O2/dL)."""
    if hemoglobin_g_dl <= 0 or pao2_mmhg < 0:
        raise ValueError("Hemoglobin has to be positive and PaO2 can't be negative.")
    if sao2 < 0 or sao2 > 1:
        raise ValueError("SaO2 should be a decimal between 0 and 1.")
    return (1.34 * hemoglobin_g_dl * sao2) + (0.003 * pao2_mmhg)


def oxygen_delivery(cardiac_output_l_min: float, arterial_oxygen_content_ml_dl: float) -> float:
    """Estimates oxygen delivery (DO2) in mL O2/min."""
    if cardiac_output_l_min <= 0 or arterial_oxygen_content_ml_dl < 0:
        raise ValueError("Cardiac output has to be positive and oxygen content can't be negative.")
    return cardiac_output_l_min * arterial_oxygen_content_ml_dl * 10
