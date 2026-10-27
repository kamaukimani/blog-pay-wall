from flask import Flask,request,session 
from flask_restful import Api
from .config import Config 
from .db import db,migrate,bcrypt 
from .models import *
from .routes import *
from flask_cors import CORS

def create_app():
    app=Flask(__name__)
    CORS(app,origins=["http://localhost:3000","http://127.0.0.1:3000"],supports_credentials=True)
    app.config.from_object(Config)

   
    app.json.compact=False 

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    api=Api(app)




    api.add_resource(ClearSession, '/clear', endpoint='clear')
    api.add_resource(Signup, '/signup', endpoint='signup')
    api.add_resource(CheckSession, '/check_session', endpoint='check_session')
    api.add_resource(Login, '/login', endpoint='login')
    api.add_resource(Logout, '/logout', endpoint='logout')
    api.add_resource(IndexArticle, '/articles', endpoint='article_list')
    api.add_resource(ShowArticle, '/articles/<int:id>', endpoint='show_article')
    api.add_resource(MemberOnlyIndex, '/members_only_articles', endpoint='member_index')
    api.add_resource(MemberOnlyArticle, '/members_only_articles/<int:id>', endpoint='member_article')

    @app.before_request
    def check_if_logged_in():

        open_access_list = [
            'clear',
            'signup',
            'article_list',
            'show_article',
            'login',
            'logout',
            'check_session'
        ]

        if (request.endpoint) not in open_access_list and (not session.get('user_id')):
            return {'error': '401 Unauthorizeddd'}, 401
   


    return app