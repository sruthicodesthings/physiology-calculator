# Physiology Calculator

A small project I made to practice Python, React, APIs, and some physiology math at the same time.

It currently has calculators for BMI, BSA, mean arterial pressure, pulse pressure, cardiac output, ventilation, P/F ratio, oxygen content, and a few unit conversions.

## Running the Python side

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
uvicorn api:app --reload
```

The API should then be at `http://localhost:8000`. FastAPI also makes docs at `http://localhost:8000/docs`.

## Running the React side

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open the address Vite prints (normally `http://localhost:5173`).

## What is in here?

- `backend/physiology/` has the actual math functions.
- `backend/api.py` lets the React website use those functions.
- `backend/tests/` checks that the math is giving the answers I expect.
- `frontend/` is the website.
