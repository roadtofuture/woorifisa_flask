from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy #sql 쿼리로 바꿔주는 orm 
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .views import basic_views, sia_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(sia_views.sia)
    return app


