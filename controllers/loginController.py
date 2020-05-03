import datetime
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

from models import *
from flask_restx import Resource

class LoginController(Resource):

  def post(self):
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    authorized = True if password =="12345" else False

    if not authorized:
      return {'error':'Email or password invalid'},401

    expires = datetime.timedelta(days=8)
    access_token = create_access_token(identity=str(1), expires_delta=expires)
    return {'token': access_token}, 200

