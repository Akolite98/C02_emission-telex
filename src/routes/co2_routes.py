from flask import Blueprint, jsonify, request
from src.services.co2_service import fetch_co2_data

co2_bp = Blueprint("co2", __name__)

@co2_bp.route("/", methods=["GET"])
def home():
    return "CO2 Monitoring API is running!"

@co2_bp.route("/co2-data", methods=["GET"])
def get_co2_data():
    country_code = request.args.get('countryCode', 'US')  # Default to 'US' if not provided
    data = fetch_co2_data(country_code)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to fetch CO2 data"}), 500
