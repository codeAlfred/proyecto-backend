from flask import request

#Modulos propios del sistema
from models import *
from flask_restx import Resource

class UserController(Resource):
  
  def get(self,id):
    user = User.query.get_or_404(id)
    return userSchema.dump(user)
  
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
   
  def delete (self,id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return userSchema.dump(user)

class UserPostController(Resource):
  
  def get(self):
    users = User.query.all()
    return userSchema.dump(users)
  
  def post(self):
    data = request.get_json()
    
    new_user = User(
      nombre=data['nombre'],
      apellido=data['apellido'],
      password = data['password'],
      email = data['email'],
      movil = data['movil'],
      fechaNacimiento = data['fechaNacimiento'],
      foto = data['foto'],
      description = data['description'],
      estado_id = data['estado_id'],
      sede_id = data['sede_id']
    )
    
    db.session.add(new_user)
    db.session.commit()
    return userSchema.dump(new_user)
  