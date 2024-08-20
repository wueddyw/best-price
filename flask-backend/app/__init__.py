from flask import Flask
from flask_cors import CORS
from .config import Config  # Import the Config class

def create_app():
    app = Flask(__name__)
    CORS(app)  # This allows all domains, which is fine for development
    
    app.config.from_object(Config)  # Load configuration from the Config class

    from .routes import main
    app.register_blueprint(main)

    return app
