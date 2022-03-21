from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from physiology.anthropometrics import bmi, bsa_mosteller, bsa_dubois
from physiology.hemodynamics import mean_arterial_pressure, pulse_pressure, cardiac_output
from physiology.respiratory import minute_ventilation, pf_ratio

app = FastAPI(title="Physiology Calculator", version="1.0")

# React runs on port 5173 when using Vite, so this lets it talk to the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def answer(value, unit):
    return {"value": round(value, 3), "unit": unit}


def run_calculation(function, unit, *values):
    try:
        return answer(function(*values), unit)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.get("/")
def home():
    return {"message": "Physiology calculator API is running!"}


@app.get("/calculate/bmi")
def calculate_bmi(weight_kg: float, height_m: float):
    return run_calculation(bmi, "kg/m^2", weight_kg, height_m)


@app.get("/calculate/bsa")
def calculate_bsa(weight_kg: float, height_cm: float, formula: str = "mosteller"):
    if formula.lower() == "dubois":
        return run_calculation(bsa_dubois, "m^2", weight_kg, height_cm)
    if formula.lower() == "mosteller":
        return run_calculation(bsa_mosteller, "m^2", weight_kg, height_cm)
    raise HTTPException(status_code=400, detail="Formula should be mosteller or dubois.")


@app.get("/calculate/map")
def calculate_map(systolic_bp: float, diastolic_bp: float):
    return run_calculation(mean_arterial_pressure, "mmHg", systolic_bp, diastolic_bp)


@app.get("/calculate/pulse-pressure")
def calculate_pp(systolic_bp: float, diastolic_bp: float):
    return run_calculation(pulse_pressure, "mmHg", systolic_bp, diastolic_bp)


@app.get("/calculate/cardiac-output")
def calculate_co(heart_rate_bpm: float, stroke_volume_ml: float):
    return run_calculation(cardiac_output, "L/min", heart_rate_bpm, stroke_volume_ml)


@app.get("/calculate/minute-ventilation")
def calculate_mv(respiratory_rate: float, tidal_volume_ml: float):
    return run_calculation(minute_ventilation, "L/min", respiratory_rate, tidal_volume_ml)


@app.get("/calculate/pf-ratio")
def calculate_pf(pao2_mmhg: float, fio2: float):
    return run_calculation(pf_ratio, "", pao2_mmhg, fio2)
