from flask_sqlalchemy import SQLAlchemy


from server import app

# importando la instancia que ejecuta la clase ConnexionBD
from connection.conexion import connexionBD


# url de la conexion a la BD
app.config['SQLALCHEMY_DATABASE_URI'] = connexionBD["URI"]
# configuracion del SQLALCHEMY en la app
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = connexionBD["TRACK_MODIFICATIONS"]
app.config["SQLALCHEMY_ECHO"] = connexionBD["ECHO"]
# instancia a SQLAlchemy
db = SQLAlchemy(app)

# importando los modelos de la base de datos
from models.userModel import *

# creando todas las tablas en la base de datos
db.create_all()



