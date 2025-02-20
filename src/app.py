from flask import Flask
from src.routes.co2_routes import co2_bp

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(co2_bp)
    
    return app
