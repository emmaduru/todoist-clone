from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from todoist.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "auth.login"

from todoist.views.auth import auth
app.register_blueprint(auth, url_prefix="/auth")

from todoist.views.project import project
app.register_blueprint(project, url_prefix="/projects")

import todoist.views.views
from todoist.models import user, project, task