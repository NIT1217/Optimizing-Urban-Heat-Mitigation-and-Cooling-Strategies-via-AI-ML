# 🌍 THERMO-ISRO
### Optimizing Urban Heat Mitigation and Cooling Strategies via AI/ML

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange)
![Mapbox](https://img.shields.io/badge/Mapbox-Interactive_Map-purple)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 🚀 Overview

THERMO-ISRO is an AI-powered Urban Heat Island (UHI) intelligence platform designed to help cities identify, predict, and mitigate extreme heat risks.

The system combines:

- 🛰️ Satellite Data
- 🌡️ Land Surface Temperature Analysis
- 🤖 Machine Learning (XGBoost)
- 🗺️ Interactive Geospatial Visualization
- 🌳 Urban Cooling Simulations
- 📊 Causal AI Insights

to provide actionable recommendations for reducing urban heat and improving climate resilience.

---

## 🎯 Problem Statement

Rapid urbanization causes:

- Increased Land Surface Temperature (LST)
- Urban Heat Island (UHI) effects
- Higher energy consumption
- Increased heat-related health risks
- Reduced environmental sustainability

Traditional approaches identify heat zones but rarely provide:

- Accurate predictions
- Root-cause analysis
- Mitigation optimization

THERMO-ISRO addresses all three.

---

## ✨ Key Features

### 🔥 Heat Risk Prediction

Predicts urban heat intensity using:

- Temperature
- Humidity
- Vegetation Index
- Land Cover
- Population Density
- Infrastructure Metrics

---

### 🗺️ Interactive Heat Map

Users can:

- Select locations on map
- View heat risk zones
- Explore urban hotspots
- Analyze vulnerable regions

---

### 🧠 Causal AI Analysis

Identifies major contributors to urban heat:

- Building Density
- Vegetation Loss
- Road Infrastructure
- Surface Materials
- Population Concentration

---

### 🌳 Intervention Simulation

Simulates the impact of:

- Cool Roofs
- Tree Plantation
- Green Spaces
- Permeable Pavements

before actual implementation.

---

### ⚡ Optimization Engine

Suggests the most effective mitigation strategy based on:

- Cost
- Cooling Effect
- Population Coverage
- Sustainability

---

## 🏗️ System Architecture

```text
Satellite Data
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
XGBoost Model
      │
      ▼
Flask API
      │
 ┌────┼───────────────┐
 ▼    ▼               ▼
Predict  Simulate  Optimize
 │       │          │
 └───────┴──────────┘
         ▼
 Web Dashboard
```

---

## 📂 Project Structure

```text
THERMO-ISRO/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── urban_heat_xgboost.pkl
│
├── data/
│   └── final_heat_dataset.csv
│
├── static/
│   ├── dashboard.css
│   ├── js/
│   │   ├── map.js
│   │   ├── api.js
│   │   ├── charts.js
│   │   ├── simulate.js
│   │   └── optimize.js
│
├── templates/
│   ├── index.html
│   ├── causal.html
│   ├── simulate.html
│   └── optimize.html
│
└── notebooks/
```

---

## 🤖 Machine Learning Model

### Algorithm

- XGBoost Regressor

### Input Features

- Temperature
- Humidity
- NDVI
- Population Density
- Road Density
- Built-Up Area
- Vegetation Coverage

### Output

- Predicted Urban Heat Intensity

---

## 📊 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Flask | API Server |
| XGBoost | ML Model |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| SHAP | Explainable AI |
| Chart.js | Data Visualization |
| Mapbox | Interactive Maps |
| HTML/CSS/JS | Frontend |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/THERMO-ISRO.git

cd THERMO-ISRO
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Visit:

```text
http://127.0.0.1:5000
```

---

## 📈 Future Enhancements

- Real-time Weather Integration
- 48-Hour Heat Forecasting
- ISRO Satellite Data Pipeline
- Climate Scenario Simulation
- Mobile Application
- Smart City Integration

---

## 🏆 Why THERMO-ISRO is Unique

Unlike traditional heat mapping systems, THERMO-ISRO:

✅ Predicts future heat risk

✅ Explains root causes using Causal AI

✅ Simulates mitigation strategies

✅ Optimizes interventions

✅ Provides decision-support for urban planners

This transforms heat monitoring into actionable climate intelligence.


## 📜 License

MIT License

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others
