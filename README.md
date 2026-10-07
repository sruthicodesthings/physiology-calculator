# Physiology Calculator

A comprehensive, lightweight JavaScript library and web interface designed for rapid clinical and academic physiological calculations. The tool provides reliable estimates for key physiological metrics across anthropometrics, cardiovascular parameters, respiratory dynamics, and unit conversions.

---

## Overview

The `physiology-calculator` project centralens standard physiological formulas into a single, dependency-free toolkit. It serves as a practical reference and computational utility for health professionals, researchers, and students needing quick, reproducible baseline estimates.

### Key Features

* **Anthropometrics & Body Composition:** Body Surface Area (BSA) via multiple standard formulas (Mosteller, Du Bois), Body Mass Index (BMI), and ideal weight metrics.
* **Cardiovascular Metrics:** Mean Arterial Pressure (MAP), Pulse Pressure, and baseline hemodynamic indices.
* **Respiratory Dynamics:** Minute Ventilation, Tidal Volume relationships, and basic oxygenation estimates.
* **Unit Conversions:** Integrated conversion utilities for pressure ($\text{mmHg} \leftrightarrow \text{kPa}$), length ($\text{cm} \leftrightarrow \text{in}$), mass ($\text{kg} \leftrightarrow \text{lb}$), and flow parameters.

---

## Interactive Formula & Metric Reference

Use the interactive reference tool below to select physiological parameters, input test values, and dynamically evaluate the corresponding equations across all system categories.

---

## Repository Structure

```text
physiology-calculator/
├── backend/
│   └── physiology/
│       ├── __init__.py
│       └── anthropometrics.py
├── .gitignore
└── README.md

```

---

## Physiological Formulas & Methodologies

| Category | Metric | Parameters | Formula / Method |
| --- | --- | --- | --- |
| **Anthropometrics** | Body Mass Index (BMI) | Mass ($m$ in $\text{kg}$), Height ($h$ in $\text{m}$) | $\text{BMI} = \frac{m}{h^2}$ |
| **Anthropometrics** | BSA (Mosteller) | Mass ($m$ in $\text{kg}$), Height ($h$ in $\text{cm}$) | $\text{BSA} = \sqrt{\frac{h \cdot m}{3600}}$ |
| **Anthropometrics** | BSA (Du Bois) | Mass ($m$ in $\text{kg}$), Height ($h$ in $\text{cm}$) | $\text{BSA} = 0.007184 \cdot h^{0.725} \cdot m^{0.425}$ |
| **Cardiovascular** | Mean Arterial Pressure | Systolic ($P_s$), Diastolic ($P_d$) | $\text{MAP} \approx P_d + \frac{1}{3}(P_s - P_d)$ |
| **Cardiovascular** | Pulse Pressure | Systolic ($P_s$), Diastolic ($P_d$) | $\text{PP} = P_s - P_d$ |
| **Respiratory** | Minute Ventilation ($\dot{V}_E$) | Tidal Volume ($V_T$ in $\text{L}$), Resp Rate ($RR$ in $\text{bpm}$) | $\dot{V}_E = V_T \cdot RR$ |

---

## Installation & Local Setup

### Prerequisites

* Python 3.8 or higher
* Standard development tools (`git`)

### Getting Started

1. **Clone the repository:**
```bash
git clone git@github.com:sruthicodesthings/physiology-calculator.git
cd physiology-calculator

```


2. **Initialize Python Environment:**
```bash
python3 -m venv venv
source venv/bin/activate

```


3. **Verify Installation:**
```bash
python3 -c "import backend.physiology; print('Physiology modules loaded successfully.')"

```



---

## Usage Examples

### Anthropometric Calculations

```python
from backend.physiology.anthropometrics import calculate_bmi, calculate_bsa_mosteller

height_cm = 175.0
weight_kg = 70.0

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_cm / 100.0)
print(f"BMI: {bmi:.2f} kg/m^2")

# Calculate Body Surface Area using Mosteller formula
bsa = calculate_bsa_mosteller(height_cm, weight_kg)
print(f"BSA (Mosteller): {bsa:.2f} m^2")

```

---

## Testing

Run unit tests across the calculation modules to verify equation accuracy:

```bash
python3 -m unittest discover -s tests

```

---

## License

This project is open source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
