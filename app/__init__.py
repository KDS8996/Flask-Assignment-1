from flask import Flask
from models import db,login_manager
from config import Config
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, static_url_path='/static')

    # Register blueprints
    from .api.routes import api
    from .site.routes import site
    from .authentication.routes import auth
    from .Cars.routes import cars_bp  # Import the cars Blueprint

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(site)
    app.register_blueprint(auth)
    app.register_blueprint(cars_bp, url_prefix='/cars')  # Register the cars Blueprint

    # Configure the Flask application
    app.config.from_object(Config)

    # Initialize extensions
    login_manager.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
