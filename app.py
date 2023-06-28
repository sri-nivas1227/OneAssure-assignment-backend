from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.premium import premium_calculator

app = Flask(__name__)

CORS(app)


@app.route("/calc-premium", methods=["POST"])
def calculate_expected_premium():
    data = request.get_json()
    age_list = data["age_list"]
    sumInsured = data["sumInsured"]
    city_tier = data["city_tier"]
    tenure = data["tenure"]
    if age_list and sumInsured and city_tier and tenure:
        try:
            expected_premium = premium_calculator(
                age_list=age_list,
                sumInsured=sumInsured,
                city_tier=city_tier,
                tenure=tenure,
            )
            res = {"status": "success", "expectedPremium": expected_premium}
            return jsonify(res), 200
        except Exception as e:
            res = {"status": "error", "message": "server error"}
            return jsonify(res), 500
    else:
        res = {"status": "error", "message": "Invalid request"}
        return jsonify(res), 400
