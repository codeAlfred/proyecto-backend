# importando el init
from . import db

import datetime

# la clase user creara la tabla users en la base de datos
class User(db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), unique=True, nullable=False)
    apellido = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(115), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    movil       = db.Column(db.String(15), unique=True, nullable=False)
    fechaNacimiento = db.Column(db.DateTime, default=datetime.datetime.now())
    foto = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())

