from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    #-- 클래스를 통채로 전달
    # print(app.config)
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    #bcrypt
    bcrypt.init_app(app)

    # Blueprint
    from .views import main_view, signup_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(signup_view.bp)

    # Model
    from todo import models

    return app

