# importando el init
from . import db,ma

import datetime

# la clase user creara la tabla users en la base de datos
class User(db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45),  nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(115), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    movil       = db.Column(db.String(15), unique=True, nullable=False)
    fechaNacimiento = db.Column(db.DateTime, default=datetime.datetime.now())
    foto = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id'))
    sede_id = db.Column(db.Integer, db.ForeignKey('sedes.id'))





class Estado(db.Model):
    __tablename__ ='estados'

    id = db.Column(db.Integer, primary_key=True)
    nombreEstado = db.Column(db.String(45), unique=True, nullable=False)
    users= db.relationship('User', backref='estado', lazy=True)

class Sede(db.Model):
    __tablename__ ='sedes'

    id = db.Column(db.Integer, primary_key=True)
    nombreSede = db.Column(db.String(100), unique=True, nullable=False)
    users= db.relationship('User', backref='sede', lazy=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","apellido","password","email","movil","fechaNacimiento","foto","description","estado_id","sede_id")

userSchema = UserSchema()
usersSchema = UserSchema(many=True)