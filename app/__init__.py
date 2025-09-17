# app/__init__.py
from flask import Flask
from .config import Config
from .models import db, migrate
from .views.ui import ui_bp
from .views.api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(ui_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
