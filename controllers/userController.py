from flask import request
from flask_jwt_extended import jwt_required#jwt

#Modulos propios del sistema
from models import *
from flask_restx import Resource

import datetime

class UserController(Resource):
  # BUSCAR un usuario por su id
  @jwt_required
  def get(self,id):
    user = User.query.get_or_404(id)
    return userSchema.dump(user)

  # ACTUALIZAR un usuario por su id
  @jwt_required
  def put(self, id):

    data = request.get_json()
    date_time_str = data['fechaNacimiento']

    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

    user = User.query.filter_by(id=id).first()
    if "nombre" in data: user.nombre = data["nombre"]
    if "apellido" in data: user.apellido = data["apellido"]
    if "password" in data: user.password = data["password"]
    if "email" in data: user.email = data["email"]
    if "movil" in data: user.movil = data["movil"]
    if "fechaNacimiento" in data: user.fechaNacimiento = date_time_obj
    if "foto" in data: user.foto = data["foto"]
    if "description" in data: user.description = data["description"]
    db.session.commit()

    user = User.query.filter_by(id=id).first()
    return userSchema.dump(user)

  #  ELIMINAR un usuario por su id
  @jwt_required
  def delete (self,id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return userSchema.dump(user)

class UserPostController(Resource):
  # LISTAR todos los usuarios
  @jwt_required
  def get(self):
    # seleccionar todos los usuarios
    users = User.query.all()
    return usersSchema.dump(users)

  # AGREGAR un usuario validando el ingreso correcto del movil ejm:+519xxxxxxxx
  @jwt_required
  def post(self):
    data = request.get_json()

    # convertir la fecha de tipo string a tipo datetime
    date_time_obj = datetime.datetime.strptime(data['fechaNacimiento'], '%Y-%m-%d')

    telefono = data["movil"]

    if len(telefono) == 12:
      if telefono[:4] == "+519":
        if telefono[4:].isnumeric():
          new_user = User(
              nombre=data['nombre'],
              apellido=data['apellido'],
              password = data['password'],
              email = data['email'],
              movil = data['movil'],
              fechaNacimiento = date_time_obj,
              foto = data['foto'],
              description = data['description'],
              estado_id = data['estado_id'],
              sede_id = data['sede_id'],
              especialidad_id = data['especialidad_id']
            )

          db.session.add(new_user)
          db.session.commit()
          return userSchema.dump(new_user)
        else:
          return {'error':'ingresar solo numeros del 0 al 9'},400
      else:
        return {'error':'el codigo postal es +51 y el movil debe comenzar con 9'},400
    else:
      return {'error':'tamaño demasiado grande para el movil'},400




class UserOrderNameOrLastNameController(Resource):
  # LISTAR todos los usuarios por orden de apellido o nombre
  def get(self, nameOrLastName):
    users=''
    if nameOrLastName == 'apellido':
      users = User.query.order_by(User.apellido).all()
    if nameOrLastName == 'nombre':
      users = User.query.order_by(User.nombre).all()

    return usersSchema.dump(users)

class UserListSpecializationController(Resource):
  # LISTAR todos los usuarios por su especialidad
  def get(self):
    data = request.get_json()
    idEspecializacion=data["idEspecialidad"]
    if validarIdEspecialidad(idEspecializacion):

      users= User.query.filter_by(especialidad_id=idEspecializacion).all()
      return usersSchema.dump(users)
    else:
      return {'error':'especialidad enviada no se encuentra en la base de datos'},400

class UserSearchController(Resource):
  # BUSCAR todos los usuarios ingresando algunas letras de su nombre
  def get(self, nombre):
    search =f'%{nombre}%'
    users = User.query.filter(User.nombre.like(search)).all()
    return usersSchema.dump(users)

class UserStateController(Resource):
  # LISTAR todos los usuarios por su estado
  def get(self):
    data = request.get_json()
    idEstado=data["idEstado"]

    if validarIdEstado(idEstado):
      if idEstado:
        users= User.query.filter_by(estado_id=idEstado).all()
      else:
        return {'error':'estado enviado no se encuentra en la base de datos'},400

      return usersSchema.dump(users)
    else:
      return {'error':'estado enviado no se encuentra en la base de datos'},400

  # ACTUALIZAR o cambiar el estado de un usuario y guarda la fecha y hora del ultimo estado de conectado
  def put(self):
    data = request.get_json()

    if validarIdUser(data['id']) and validarIdEstado(data['idEstado']):
      user = User.query.filter_by(id=data['id']).first()
      dic_user=userSchema.dump(user)
      if "idEstado" in data:
        user.estado_id = data['idEstado']
        if dic_user["estado_id"] == 1 and  data['idEstado']>1:
          user.last_connection=datetime.datetime.now()
      else:
        return {'error':'nombre del campo incorrecto'},400

      db.session.commit()

      user = User.query.filter_by(id=data['id']).first()
      return userSchema.dump(user)
    else:
       return {'error':'usuario o estado no encontrado en la base de datos'},400

class UserLastConnectionController(Resource):
  # MOSTRAR la ultima conexion activa
  def get(self):

    data = request.get_json()
    if validarIdUser(data['idUser']):
      user = User.query.filter_by(id=data['idUser']).first()

      return userSchema.dump(user)
    else:
      return {'error':'usuario no encontrado en la base de datos'},400

# validar que el id del usuario enviado se encuentre en la base de datos
def validarIdUser(idUser):

  user=User.query.with_entities(User.id)
  lista=usersSchema.dump(user)
  ids=[]
  for diccionario in lista:
    for key, value in diccionario.items():
      ids.append(value)

  if idUser in ids:
    return True
  else:
    return False
  
# validar que el id del estado enviado se encuentre en la base de datos
def validarIdEstado(idEstado):

  estado=Estado.query.with_entities(Estado.id)
  lista=estadosSchema.dump(estado)
  ids=[]
  for diccionario in lista:
    for key, value in diccionario.items():
      ids.append(value)

  if idEstado in ids:
    return True
  else:
    return False

# validar que el id del estado enviado se encuentre en la base de datos
def validarIdEspecialidad(idEspecialidad):

  especialidad=Especialidad.query.with_entities(Especialidad.id)
  lista=especialidadesSchema.dump(especialidad)
  ids=[]
  for diccionario in lista:
    for key, value in diccionario.items():
      ids.append(value)

  if idEspecialidad in ids:
    return True
  else:
    return False


