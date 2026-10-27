from flask_restful import Resource
from flask import session,request,make_response,jsonify
from app.models import User
from flask_bcrypt import Bcrypt 
from app.db import db

bcrypt=Bcrypt()



class Signup(Resource):

    def post(self):
        data=request.get_json()

        username = data["username"]
        email = data.get("email")
        password = data["password"]
        password_confirmation=data.get("password_confirmation")

        if password != password_confirmation:
            return {"error":"Passwords do not match!!!"},401


        
        if username and email and password:
            
            new_user = User(username=username)
            new_user.email=email
            new_user.password=bcrypt.generate_password_hash(password).decode("utf-8")
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
            
            return new_user.to_dict(), 201

        return {'error': 'Invalid email or password'}, 422

class CheckSession(Resource):

    def get(self):

        if session.get('user_id'):
            
            user = User.query.filter(User.id == session['user_id']).first()
            
            return user.to_dict(), 200

        return {"error":"Unauthorized"}, 401

class Login(Resource):

    def post(self):
        data=request.get_json()

        #username = data["username"]
        email = data.get("email")
        password = data["password"]

        user = User.query.filter(User.email == email).first()
        if not user:
            return {"error": "Invalid email or password"},401

        is_hashed=bcrypt.check_password_hash(user.password,password)

        if is_hashed:

            session['user_id'] = user.id
            return user.to_dict(rules=("-password",)), 200

        return {"error": "Invalid email or password"}, 401

class Logout(Resource):

    def delete(self):

        session['user_id'] = None

        return {}, 204