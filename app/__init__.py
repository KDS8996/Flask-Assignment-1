from flask import Flask
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config
from models import db, ma, login_manager 
from flask_migrate import Migrate

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)
db.init_app(app) 
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)