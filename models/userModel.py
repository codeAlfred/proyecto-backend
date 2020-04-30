# agregando configuracion de alchemy
from connection.conexion import connexionBD
from flask_sqlalchemy import SQLAlchemy
import datetime
# from main import app
# url de la conexion a la BD
app.config['SQLALCHEMY_DATABASE_URI'] = connexionBD["URI"]

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = connexionBD["TRACK_MODIFICATIONS"]
app.config["SQLALCHEMY_ECHO"] = connexionBD["ECHO"]
# instancia a SQLAlchemy
db = SQLAlchemy(app)

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

db.create_all()