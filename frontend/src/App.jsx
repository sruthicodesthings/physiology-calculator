import { useState } from "react";

export default function App() {
  const [weight, setWeight] = useState("");
  const [height, setHeight] = useState("");
  const [answer, setAnswer] = useState("");

  async function calculateBMI() {
    const response = await fetch(`http://localhost:8000/calculate/bmi?weight_kg=${weight}&height_m=${height}`);
    const data = await response.json();
    setAnswer(`${data.value} ${data.unit}`);
  }

  return (
    <main>
      <h1>Physiology Calculator</h1>
      <h2>BMI</h2>
      <input placeholder="weight in kg" value={weight} onChange={(e) => setWeight(e.target.value)} />
      <input placeholder="height in m" value={height} onChange={(e) => setHeight(e.target.value)} />
      <button onClick={calculateBMI}>calculate</button>
      <p>{answer}</p>
    </main>
  );
}
