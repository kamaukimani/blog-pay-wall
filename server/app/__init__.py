from flask import Flask,request,session 
from flask_restfu import Api
from .config import Config 
from .db import db,migrate,bcrypt 

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)
    app.json.compact=False 

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    api=Api(app)


    return app