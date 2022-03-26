import { useState } from "react";

const API = "http://localhost:8000";

const calculators = [
  { name: "BMI", path: "bmi", fields: [["Weight (kg)", "weight_kg"], ["Height (m)", "height_m"]] },
  { name: "BSA (Mosteller)", path: "bsa", fields: [["Weight (kg)", "weight_kg"], ["Height (cm)", "height_cm"]] },
  { name: "Mean Arterial Pressure", path: "map", fields: [["Systolic BP", "systolic_bp"], ["Diastolic BP", "diastolic_bp"]] },
  { name: "Pulse Pressure", path: "pulse-pressure", fields: [["Systolic BP", "systolic_bp"], ["Diastolic BP", "diastolic_bp"]] },
  { name: "Cardiac Output", path: "cardiac-output", fields: [["Heart rate (bpm)", "heart_rate_bpm"], ["Stroke volume (mL)", "stroke_volume_ml"]] },
  { name: "Minute Ventilation", path: "minute-ventilation", fields: [["Respiratory rate", "respiratory_rate"], ["Tidal volume (mL)", "tidal_volume_ml"]] },
  { name: "P/F Ratio", path: "pf-ratio", fields: [["PaO2 (mmHg)", "pao2_mmhg"], ["FiO2 (decimal)", "fio2"]] }
];

function Calculator({ calculator }) {
  const [values, setValues] = useState({});
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function calculate() {
    setError("");
    setResult(null);
    const params = new URLSearchParams(values);
    try {
      const response = await fetch(`${API}/calculate/${calculator.path}?${params}`);
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Something went wrong.");
      setResult(data);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <section className="card">
      <h2>{calculator.name}</h2>
      {calculator.fields.map(([label, key]) => (
        <label key={key}>{label}
          <input type="number" step="any" onChange={(e) => setValues({...values, [key]: e.target.value})} />
        </label>
      ))}
      <button onClick={calculate}>Calculate</button>
      {result && <p className="result">Answer: {result.value} {result.unit}</p>}
      {error && <p className="error">{error}</p>}
    </section>
  );
}

export default function App() {
  return (
    <main>
      <h1>Physiology Calculator</h1>
      <p className="intro">Some useful body and physiology calculations I put together while learning Python and React.</p>
      <p className="note">For learning only — this isn't medical advice.</p>
      <div className="grid">{calculators.map((c) => <Calculator key={c.name} calculator={c} />)}</div>
    </main>
  );
}
