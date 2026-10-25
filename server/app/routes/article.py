from flask_restful import Resource
from flask import session,request,make_response,jsonify
from app.models import Article



class ClearSession(Resource):

    def delete(self):
    
        session['page_views'] = None
        session['user_id'] = None

        return {}, 204

class IndexArticle(Resource):
    
    def get(self):
        articles = [article.to_dict() for article in Article.query.all()]
        return make_response(jsonify(articles), 200)

class ShowArticle(Resource):

    def get(self, id):

        article = Article.query.filter(Article.id == id).first()
        article_json = article.to_dict()

        if not session.get('user_id'):
            session['page_views'] = 0 if not session.get('page_views') else session.get('page_views')
            session['page_views'] += 1

            if session['page_views'] <= 3:
                return article_json, 200

            return make_response(
                jsonify({
                    'message': 'Maximum pageview limit reached'
                }),
                401
            )

        return article_json, 200



class MemberOnlyIndex(Resource):
    
    def get(self):
    
        articles = Article.query.filter(Article.is_member_only == True).all()
        return [article.to_dict() for article in articles], 200

class MemberOnlyArticle(Resource):
    
    def get(self, id):

        article = Article.query.filter(Article.id == id).first()
        return article.to_dict(), 200