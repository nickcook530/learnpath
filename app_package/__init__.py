from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_bootstrap import Bootstrap

#initiatlize app
app = Flask(__name__)
app.config.from_object(Config)

#initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True) #compare_type=true picks up on column type changes
login_manager = LoginManager(app)
#bootstrap = Bootstrap(app)

#initiatilize blueprints
from .oauth import blueprint
app.register_blueprint(blueprint, url_prefix="/login")

#imports at bottom to avoid circular imports
from app_package import routes, models