from . import data_access_layer as DAL
import web
from web import Appication,NestableBlueprint,jsonify
# from flask.views import MethodView,View
import json
from web.restful import Resource

class UserAPI(Resource):
    Model=DAL.User



def create_app():
    app=Appication(__name__)
    app=UserAPI.register_api(app,endpoint='user_api',url='/users/',pk='resource_id',pk_type='string')
    return app


