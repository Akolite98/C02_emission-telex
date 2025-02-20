from flask import Blueprint

co2_bp = Blueprint("co2", __name__)

@co2_bp.route("/", methods=["GET"])
def home():
    return "CO2 Monitoring API is running!"
