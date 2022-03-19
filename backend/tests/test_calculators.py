import pytest

from physiology.anthropometrics import bmi, bsa_mosteller, bsa_dubois
from physiology.hemodynamics import mean_arterial_pressure, pulse_pressure, cardiac_output, cardiac_index
from physiology.respiratory import minute_ventilation, alveolar_ventilation, pf_ratio
from physiology.oxygen import arterial_oxygen_content, oxygen_delivery


def test_bmi():
    assert bmi(70, 1.75) == pytest.approx(22.8571, rel=1e-4)


def test_bsa():
    assert bsa_mosteller(70, 175) == pytest.approx(1.8447, rel=1e-4)
    assert bsa_dubois(70, 175) == pytest.approx(1.8481, rel=1e-4)


def test_blood_pressure_math():
    assert mean_arterial_pressure(120, 80) == pytest.approx(93.3333, rel=1e-4)
    assert pulse_pressure(120, 80) == 40


def test_heart_math():
    co = cardiac_output(70, 70)
    assert co == pytest.approx(4.9)
    assert cardiac_index(co, 1.84) == pytest.approx(2.663, rel=1e-3)


def test_lung_math():
    assert minute_ventilation(12, 500) == 6
    assert alveolar_ventilation(12, 500, 150) == pytest.approx(4.2)
    assert pf_ratio(100, 0.21) == pytest.approx(476.19, rel=1e-3)


def test_oxygen_math():
    cao2 = arterial_oxygen_content(15, 0.98, 100)
    assert cao2 == pytest.approx(20.0, rel=0.02)
    assert oxygen_delivery(5, cao2) == pytest.approx(cao2 * 50)


def test_bad_inputs():
    with pytest.raises(ValueError):
        bmi(70, 0)
    with pytest.raises(ValueError):
        mean_arterial_pressure(70, 100)
    with pytest.raises(ValueError):
        pf_ratio(100, 1.2)
