import datetime
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

from models import *
from flask_restx import Resource

import datetime

class LoginController(Resource):

  def post(self):
    data = request.get_json()
    # obtener el email y password enviado en el JSON
    email = data.get("email")
    password = data.get("password")
    # buscar al usuario por medio de su email (el email es unico)
    user= User.query.filter_by(email=email).first()
    # formatear el usuario a un diccionario
    user1=userSchema.dump(user)
    # validar si el email y password son iguales
    authorized = True if user1['password'] == password and user1['email'] == email else False
    # authorized = True if password =="12345" else False

    if not authorized:
      return {'error':'Email or password invalid'},401
    else:
      # cambiar el estado a conectado
      idEstado=1
      user.estado_id = idEstado
       # agregar la fecha de conexion a la hora de logearse
      new_conexion=Conexion(
        user_id=user1['id'],
        create_At= datetime.datetime.now()
      )
      db.session.add(new_conexion)

      db.session.commit()

    expires = datetime.timedelta(days=8)
    access_token = create_access_token(identity=str(1), expires_delta=expires)
    return {'token': access_token}, 200

