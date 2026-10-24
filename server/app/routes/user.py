from flask_restful import Resource
from flask import session,request,make_response,jsonify
from app.models import User
from flask_bcrypt import Bcrypt 

bcrypt=Bcrypt()



class Signup(Resource):

    def post(self):
        data=request.get_json()

        username = data["username"]
        email = data.get("email")
        password = data["password"]


        
        if username,email and password:
            
            new_user = User(username=username)
            new_user.email=email
            new_user.password=bcrypt.generate_password_hash(password).decode("utf-8")
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
            
            return new_user.to_dict(), 201

        return {'error': '422 Unprocessable Entity'}, 422

class CheckSession(Resource):

    def get(self):

        if session.get('user_id'):
            
            user = User.query.filter(User.id == session['user_id']).first()
            
            return user.to_dict(), 200

        return {}, 204

class Login(Resource):

    def post(self):
        data=request.get_json()

        username = data["username"]
        email = data.get("email")
        password = data["password"]

        user = User.query.filter(User.email == email).first()

        is_hashed=bcrypt.check_password_hash(user.password,password)

        if is_hashed:

            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):

    def delete(self):

        session['user_id'] = None

        return {}, 204