from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

# ==========================================
# PAGE ROUTES
# ==========================================

@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/causal")
def causal():
    return render_template("causal.html")


@app.route("/simulate")
def simulate():
    return render_template("simulate.html")


@app.route("/optimize")
def optimize():
    return render_template("optimize.html")


# ==========================================
# API ROUTES
# ==========================================

@app.route("/api/predict")
def predict():

    data = {
        "city": "Chennai",
        "current_temp": 45.7,
        "forecast": [46,47,48,49,48,47,46]
    }

    return jsonify(data)


@app.route("/api/causal")
def causal_analysis():

    data = {
        "drivers": [
            {
                "name": "Building Density",
                "impact": 0.89
            },
            {
                "name": "Vegetation",
                "impact": 0.77
            },
            {
                "name": "Traffic",
                "impact": 0.63
            },
            {
                "name": "Population",
                "impact": 0.58
            }
        ]
    }

    return jsonify(data)


@app.route("/api/simulate", methods=["POST"])
def run_simulation():

    payload = request.get_json()

    roofs = payload["cool_roofs"]
    trees = payload["tree_canopy"]
    pavements = payload["permeable"]

    cooling = (
        roofs * 0.012 +
        trees * 0.018 +
        pavements * 0.009
    )

    cost = (
        roofs * 150000 +
        trees * 220000 +
        pavements * 100000
    )

    population = (
        roofs * 700 +
        trees * 1100 +
        pavements * 450
    )

    return jsonify({
        "temperature_drop": round(cooling,2),
        "cost": cost,
        "population": population
    })


@app.route("/api/optimize")
def optimize_budget():

    result = {
        "recommended_plan": {
            "cool_roofs": 65,
            "tree_canopy": 82,
            "permeable": 40
        },
        "cooling": 3.4,
        "budget": 12500000
    }

    return jsonify(result)


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )