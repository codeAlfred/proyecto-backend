from flask import request

#Modulos propios del sistema
from models import *
from flask_restx import Resource

import datetime

class UserController(Resource):
  # BUSCAR un usuario por su id
  def get(self,id):
    user = User.query.get_or_404(id)
    return userSchema.dump(user)
  
  # ACTUALIZAR un usuario por su id
  def put(self, id):
    data = request.get_json()
    user = User.query.filter_by(id=id).first()
    if "nombre" in data: user.nombre = data["nombre"]
    if "apellido" in data: user.apellido = data["apellido"]
    if "password" in data: user.password = data["password"]
    if "email" in data: user.email = data["email"]
    if "movil" in data: user.movil = data["movil"]
    if "fechaNacimiento" in data: user.fechaNacimiento = data["fechaNacimiento"]
    if "foto" in data: user.foto = data["foto"]
    if "description" in data: user.description = data["description"]
    db.session.commit()
    
    user = User.query.filter_by(id=id).first()
    return userSchema.dump(user)
  
  #  ELIMINAR un usuario por su id
  def delete (self,id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return userSchema.dump(user)

class UserPostController(Resource):
  # LISTAR todos los usuarios
  def get(self):
    # seleccionar todos los usuarios
    users = User.query.all()
    return usersSchema.dump(users)
  
  # AGREGAR un usuario
  def post(self):
    data = request.get_json()
    # recibir la fecha con formato aaaa-mm-dd
    date_time_str = data['fechaNacimiento']
    # convertir la fecha de tipo string a tipo datetime
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
    
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
      sede_id = data['sede_id']
    )
    
    db.session.add(new_user)
    db.session.commit()
    return userSchema.dump(new_user)
  

class UserOrderController(Resource):
  # LISTAR todos los usuarios por orden de apellido
  def get(self, orden):
    # ordenar usuarios
    users=''
    if orden == 'apellido':
      users = User.query.order_by(User.apellido).all()

    if orden == 'nombre':
      users = User.query.order_by(User.nombre).all()

    return usersSchema.dump(users)

class UserSearchController(Resource):
  # LISTAR todos los usuarios por orden de apellido
  def get(self, nombre):
    # ordenar usuarios
    name = nombre
    search ="%{}%".format(name)
    users = User.query.filter(User.nombre.like(search)).all()
    return usersSchema.dump(users)